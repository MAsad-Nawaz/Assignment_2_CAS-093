## Task 01 -- Combine all text in one single txt file
import pandas as pd
import os

# List of CSV file paths
file_paths = ['./csv/CSV1.csv', './csv/CSV2.csv','./csv/CSV3.csv' ,'./csv/CSV4.csv'] 

# Initialize an empty list to store texts
all_texts = []

# Iterate through each file path
for file_path in file_paths:
    if os.path.exists(file_path):  # Check if file exists
        try:
            # Read the CSV file
            df = pd.read_csv(file_path)
            
            # Check if the column 'TEXT' exists and extract it
            if 'TEXT' in df.columns:
                # Extract the 'TEXT' column, drop any missing values, and convert to list
                all_texts.extend(df['TEXT'].dropna().tolist())
            else:
                print(f"Column 'TEXT' not found in {file_path}")
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    else:
        print(f"File not found: {file_path}")

# Combine all the texts into a single string
combined_text = '\n'.join(all_texts)

# Save the combined text to a .txt file
output_path = 'combined_texts.txt'  # Specify the path where you want to save the file
with open(output_path, 'w', encoding='utf-8') as file:
    file.write(combined_text)

print(f"Combined texts have been saved to {output_path}")

