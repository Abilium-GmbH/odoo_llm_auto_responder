from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="deutsche-telekom/bert-multi-english-german-squad2",
    tokenizer="deutsche-telekom/bert-multi-english-german-squad2"
)

contexts = [
    "Abilium entwickelt und verwendet neueste Technologien und Standards um so die Probleme der Kundinnen kostengünstig und effizient zu lösen. Die Abilium GmbH ist ein Berner Technologie-Unternehmen, welches im Jahr 2016 von zwei Studierenden der Universität Bern gegründet wurde. Durch den engen Bezug zur Universität verfügt Abilium über hochqualifizierte Mitarbeiter in den Bereichen Soft- und Hardware-Entwicklung, Beratung und DevOps. Wir sind Spezialisten für die Entwicklung und den Betrieb von skalierbaren Webapplikationen, Smartphone Apps und Embedded Hardware, insbesondere IoT-Anwendungen. Unsere Firma wird von unseren Kunden als dynamisch und unkompliziert wahrgenommen, was sich besonders in der Flexibilität bei der Umsetzung der Projekte widerspiegelt. Ohne starre oder einschränkende Prozesse ermöglichen wir unseren Kunden auch während der Entwicklung ihre Wünsche einzubringen, so dass die Produkte tatsächlich ihren Bedürfnissen entsprechen.Für Bereiche, die nicht Teil unseres Kerngeschäfts sind, steht uns ein Netzwerk von spezialisierten Partnern zur Verfügung, mit denen wir bereits etliche Projekte zum Erfolg führen durften.",
    "Harvard is a large, highly residential research university. It operates several arts, cultural, and scientific museums, alongside the Harvard Library, which is the world's largest academic and private library system, comprising 79 individual libraries with over 18 million volumes. "]
questions = ["Was macht Abilium?",
             "What is the worlds largest academic and private library system?"]

print(qa_pipeline(context=contexts, question=questions))

