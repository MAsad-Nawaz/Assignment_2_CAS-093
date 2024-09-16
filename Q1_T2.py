import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import spacy

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

# Step 1: Read and preprocess the text file using NLTK

# Path to your combined text file
file_path = 'combined_texts_corrected.txt'  # Replace with your actual file path

# Read the content of the text file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Tokenize the text into words
tokens = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Print the first few tokens to check preprocessing
print("First 20 preprocessed tokens:")
print(filtered_tokens[:20])

# Step 2: Extract entities using SciSpaCy

# Load the SciSpaCy model for NER (recognizes biomedical entities like diseases, chemicals, etc.)
nlp_ner = spacy.load("en_ner_bc5cdr_md")

# Apply the SciSpaCy NER model to the text
doc = nlp_ner(text)

print("\nEntities recognized by SciSpaCy:")
# Extract and print named entities (like diseases or chemicals)
for entity in doc.ents:
    print(f"Entity: {entity.text}, Label: {entity.label_}")

# Step 3: Extract entities using BioBERT

# Load the BioBERT tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-base-cased-v1.1")

# Create a pipeline for named entity recognition using BioBERT
nlp = pipeline("ner", model=model, tokenizer=tokenizer)

# Apply the BioBERT NER model to the text
entities = nlp(text)

print("\nEntities recognized by BioBERT:")
# Print the detected entities
for entity in entities:
    print(f"Entity: {entity['word']}, Score: {entity['score']}, Label: {entity['entity']}")
