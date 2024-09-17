from transformers import AutoTokenizer
from collections import Counter

# Load the BioBERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")

# Function to count unique tokens
def count_unique_tokens(file_path):
    # Read the content of the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text using AutoTokenizer
    tokens = tokenizer.tokenize(text)
    
    # Count the occurrences of each token
    token_counts = Counter(tokens)
    
    # Get the top 30 most common tokens
    top_30_tokens = token_counts.most_common(30)
    
    # Display the results
    print("Top 30 most common tokens:")
    for token, count in top_30_tokens:
        print(f"Token: {token}, Count: {count}")

    # Return the top 30 tokens and their counts
    return top_30_tokens

# Specify the path to your combined text file
file_path = 'combined_texts.txt'

# Call the function
top_30_tokens = count_unique_tokens(file_path)
