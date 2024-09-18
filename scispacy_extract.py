import spacy

#Load SciSpaCy models
nlp_sci_sm = spacy.load("en_core_sci_sm")
nlp_bc5cdr_md = spacy.load("en_ner_bc5cdr_md")

def extract_scispacy(text, chunk_size=100000, model_name="en_core_sci_sm"):
    if model_name == "en_core_sci_sm":
        model = spacy.load("en_core_sci_sm")
    elif model_name == "en_ner_bc5cdr_md":
        model = spacy.load("en_ner_bc5cdr_md")
    else:
        raise ValueError("Invalid model name provided.")
    
    diseases, drugs = [], []
    
    #Process the text in chunks
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        doc = model(chunk)
        
        diseases.extend([ent.text for ent in doc.ents if ent.label_ == "DISEASE"])
        drugs.extend([ent.text for ent in doc.ents if ent.label_ == "CHEMICAL"])
    
    return diseases, drugs
