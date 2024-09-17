import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from collections import Counter
import pandas as pd

# Step 1: Extract Entities using SciSpaCy
print("Loading SciSpaCy model...")
nlp_sci = spacy.load("en_ner_bc5cdr_md")

# Read the combined text file
file_path = 'combined_texts.txt'  # Replace with your actual file path
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Apply the SciSpaCy NER model to the text
doc_sci = nlp_sci(text)

# Extract disease and drug entities
disease_entities_sci = [entity.text for entity in doc_sci.ents if entity.label_ == 'DISEASE']
drug_entities_sci = [entity.text for entity in doc_sci.ents if entity.label_ == 'CHEMICAL']

print("\nEntities recognized by SciSpaCy:")
print(f"Total diseases detected: {len(disease_entities_sci)}")
print(f"Total drugs detected: {len(drug_entities_sci)}")

# Step 2: Extract Entities using BioBERT
print("\nLoading BioBERT model...")
tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-base-cased-v1.1")

# Create a pipeline for named entity recognition using BioBERT
nlp_biobert = pipeline("ner", model=model, tokenizer=tokenizer)

print("\nApplying BioBERT NER model...")
entities_biobert = nlp_biobert(text)

# Filter disease and drug entities based on their labels
disease_entities_biobert = [entity['word'] for entity in entities_biobert if 'disease' in entity['entity'].lower()]
drug_entities_biobert = [entity['word'] for entity in entities_biobert if 'chemical' in entity['entity'].lower()]

print("\nEntities recognized by BioBERT:")
print(f"Total diseases detected: {len(disease_entities_biobert)}")
print(f"Total drugs detected: {len(drug_entities_biobert)}")

# Step 3: Compare Entities from Both Models
def compare_entities(entities_sci, entities_biobert):
    sci_counter = Counter(entities_sci)
    biobert_counter = Counter(entities_biobert)
    
    # Find common entities
    common_entities = set(entities_sci).intersection(set(entities_biobert))
    
    # Find entities unique to each model
    unique_sci = set(entities_sci) - common_entities
    unique_biobert = set(entities_biobert) - common_entities

    print("\nComparison Results:")
    print(f"Common entities between SciSpaCy and BioBERT: {len(common_entities)}")
    print(f"Entities unique to SciSpaCy: {len(unique_sci)}")
    print(f"Entities unique to BioBERT: {len(unique_biobert)}")

    return common_entities, unique_sci, unique_biobert

# Compare disease entities
common_diseases, unique_sci_diseases, unique_biobert_diseases = compare_entities(disease_entities_sci, disease_entities_biobert)

# Compare drug entities
common_drugs, unique_sci_drugs, unique_biobert_drugs = compare_entities(drug_entities_sci, drug_entities_biobert)
