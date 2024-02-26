from transformers import pipeline
import time

prompt = "What is odoo?"
pipe = pipeline(model="declare-lab/flan-alpaca-large")
# pipe = pipeline(model="declare-lab/flan-alpaca-gpt4-xl")
t0=time.time()
outputs = pipe(prompt, max_length=128, do_sample=True)
print(outputs[0]["generated_text"])
print('Response time:', time.time()-t0)