import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import spacy
from tqdm import tqdm  # Add tqdm for progress logging

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

# Step 1: Read and preprocess the text file using NLTK

# Path to your combined text file
file_path = '/content/sample_data/combined_texts.txt'  # Replace with your actual file path

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

print("\nLoading SciSpaCy model...")
# Load the SciSpaCy model for NER (recognizes biomedical entities like diseases, chemicals, etc.)
nlp_ner = spacy.load("en_ner_bc5cdr_md")

# Function to split text into manageable chunks
def chunk_text(text, max_length):
    """
    Split text into smaller chunks of a specified maximum length.
    """
    for i in range(0, len(text), max_length):
        yield text[i:i + max_length]

# Adjust the max_length to a smaller size that is safe to process
max_chunk_length = 1000000  # You can adjust this value

# Split the text into smaller chunks
text_chunks = list(chunk_text(text, max_chunk_length))

# Process each chunk separately with SciSpaCy
for idx, chunk in enumerate(text_chunks):
    doc = nlp_ner(chunk)
    print(f"\nEntities recognized by SciSpaCy in chunk {idx + 1}:")
    for entity in tqdm(doc.ents, desc=f"Processing entities with SciSpaCy in chunk {idx + 1}"):
        print(f"Entity: {entity.text}, Label: {entity.label_}")

# Step 3: Extract entities using BioBERT

print("\nLoading BioBERT model...")
# Load the BioBERT tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-base-cased-v1.1")

# Create a pipeline for named entity recognition using BioBERT
nlp = pipeline("ner", model=model, tokenizer=tokenizer)

print("\nApplying BioBERT NER model...")
# Process each chunk separately with BioBERT
for idx, chunk in enumerate(text_chunks):
    entities = nlp(chunk)
    print(f"\nEntities recognized by BioBERT in chunk {idx + 1}:")
    for entity in tqdm(entities, desc=f"Processing entities with BioBERT in chunk {idx + 1}"):
        print(f"Entity: {entity['word']}, Score: {entity['score']}, Label: {entity['entity']}")
