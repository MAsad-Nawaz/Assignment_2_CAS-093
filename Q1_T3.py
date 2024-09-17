import pandas as pd
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Step 1: Read the combined text file
file_path = 'combined_texts.txt'  # Replace with your actual file path

# Read the content of the text file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Step 2: Tokenize the text into words
tokens = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words]

# Step 3: Count word occurrences using Counter from collections
word_counts = Counter(filtered_tokens)

# Get the top 30 most common words
top_30_words = word_counts.most_common(30)

# Convert the top 30 words and their counts into a DataFrame
df_top_words = pd.DataFrame(top_30_words, columns=['Word', 'Count'])

# Step 4: Save the DataFrame to a CSV file
output_csv_path = 'top_30_common_words.csv'
df_top_words.to_csv(output_csv_path, index=False)

print(f"Top 30 most common words have been saved to {output_csv_path}")
