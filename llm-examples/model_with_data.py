# source: https://github.com/jeremy-k3/notebooks/blob/main/RAG_Langchain_Zephyr_DeciLM.ipynb

from langchain import document_loaders as dl
from langchain import embeddings
from langchain import text_splitter as ts
from langchain import vectorstores as vs
from langchain.llms import HuggingFacePipeline
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.runnable import RunnableParallel
from langchain.prompts import PromptTemplate
from operator import itemgetter

import torch
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM

import re
import time

document_path ="data/odoo_intro.pdf"

def split_doc(document_path, chunk_size=500, chunk_overlap=20):
    loader = dl.PyPDFLoader(document_path)
    document = loader.load()
    text_splitter = ts.RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    document_splitted = text_splitter.split_documents(documents=document)
    return document_splitted

document_splitted = split_doc(document_path)
for doc in document_splitted:
  print(doc)


from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

model.save('sentence-transformers')
del model

def load_embedding_model():
    # model_kwargs = {'device': 'cuda:0'}
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    embedding_model_instance = embeddings.HuggingFaceEmbeddings(
        model_name="sentence-transformers",
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    return embedding_model_instance

#Instantiate the embedding model
embedding_model_instance = load_embedding_model()

def create_db(document_splitted, embedding_model_instance):

    model_vectorstore = vs.FAISS
    db=None
    try:
        content = []
        metadata = []
        for d in document_splitted:
            content.append(d.page_content)
            metadata.append({'source': d.metadata})
        db=model_vectorstore.from_texts(content, embedding_model_instance, metadata)
    except Exception as error:
        print(error)
    return db

db = create_db(document_splitted, embedding_model_instance)
#store the db locally for future use
db.save_local('db.index')


# #Save the model locally.
# tokenizer = AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta")
# model = AutoModelForCausalLM.from_pretrained("HuggingFaceH4/zephyr-7b-beta", low_cpu_mem_usage=True, torch_dtype=torch.float16)
# model.save_pretrained('zephyr-7b-beta-model', max_shard_size="1000MB")
# tokenizer.save_pretrained('zephyr-7b-beta-tokenizer')
# del model
# del tokenizer
# # torch.cuda.empty_cache()
     
# #Create a pipeline with the local version of the model
# tokenizer = AutoTokenizer.from_pretrained("zephyr-7b-beta-tokenizer")
# model = AutoModelForCausalLM.from_pretrained("zephyr-7b-beta-model", low_cpu_mem_usage=True, torch_dtype=torch.float16)
# # pipe = pipeline(task="text-generation", model=model,tokenizer=tokenizer, device="cuda:0", max_new_tokens=1000)
# pipe = pipeline(task="text-generation", model=model,tokenizer=tokenizer, device="cpu", max_new_tokens=1000)

from transformers import AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("declare-lab/flan-alpaca-gpt4-xl")
model = AutoModelForSeq2SeqLM.from_pretrained("declare-lab/flan-alpaca-gpt4-xl", low_cpu_mem_usage=True, torch_dtype=torch.float16)
model.save_pretrained('flan-alpaca-gpt4-xl-model', max_shard_size="1000MB")
tokenizer.save_pretrained('flan-alpaca-gpt4-xl-tokenizer')
del model
del tokenizer

tokenizer = AutoTokenizer.from_pretrained("flan-alpaca-gpt4-xl-tokenizer")
model = AutoModelForSeq2SeqLM.from_pretrained("flan-alpaca-gpt4-xl-model", low_cpu_mem_usage=True, torch_dtype=torch.float16)
pipe = pipeline(task="text2text-generation", model=model,tokenizer=tokenizer, device="cpu", max_new_tokens=254)

#Use the pipeline in Langchain
llm=HuggingFacePipeline(pipeline=pipe, model_kwargs={'temperature': 0.2})

query = "What is Odoo?"
retriever = db.as_retriever(search_type="similarity_score_threshold", search_kwargs={"k": 6, 'score_threshold': 0.01})
retrieved_docs = retriever.get_relevant_documents(query)

template = """Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
{context}
Question: {question}
Helpful Answer:"""
rag_prompt_custom = PromptTemplate.from_template(template)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

#First chain to query the LLM
rag_chain_from_docs = (
    {
        "context": lambda input: format_docs(input["documents"]),
        "question": itemgetter("question"),
    }
    | rag_prompt_custom
    | llm
    | StrOutputParser()
)

#Second chain to postprocess the answer
rag_chain_with_source = RunnableParallel(
    {"documents": retriever, "question": RunnablePassthrough()}
) | {
    "documents": lambda input: [print(doc.metadata) or doc.metadata for doc in input["documents"]],
    "answer": rag_chain_from_docs,
}

t0=time.time()
resp = rag_chain_with_source.invoke(query)
if len(resp['documents'])==0:
  print('No documents found')
else:
  stripped_resp = re.sub(r"\n+$", " ", resp['answer'])
  print(stripped_resp)
  print('Sources',resp['documents'])
  print('Response time:', time.time()-t0)