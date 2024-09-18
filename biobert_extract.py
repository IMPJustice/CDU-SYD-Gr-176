from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Load BioBERT model and tokenizer
tokenizer_biobert = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
model_biobert = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
nlp_biobert = pipeline("ner", model=model_biobert, tokenizer=tokenizer_biobert, aggregation_strategy="simple")

def extract_biobert(text,chunk_size=512):
    ner_results = []
    
    #Process text in chunks
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        ner_results.extend(nlp_biobert(chunk))
    
    diseases = [entity['word'] for entity in ner_results if "disease" in entity['entity'].lower()]
    drugs = [entity['word'] for entity in ner_results if "drug" in entity['entity'].lower()]
    
    return diseases, drugs
