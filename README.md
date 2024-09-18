# Assignment_2

## Unit: HIT137 SOFTWARE NOW 

### Group: CAS 093

## Group Members

- **Musrat Jahan** (ID: S380098)
- **Muhammad Ahsan Butt** (ID: S380510)
- **Muhammad Asad Nawaz** (ID: S380509)
- **MD Arafath Islam Abir** (ID: S381312)


## Overview
This assignment tests python programming skills through a series of tasks involving NLP, image, string, error-prone code fixing, and collaborative work on GitHub.

## Question 1: Natural Language Processing (NLP)

### Task 1: Extract Text
- Extract the 'text' from multiple CSV files and store the extracted text into a single `.txt` file.

### Task 2: Install Libraries
- Install the following NLP libraries:
  - **SpaCy (scispaCy)**: Install models such as `en_core_sci_sm` and `en_ner_bc5cdr_md`.
  - **Transformers (Hugging Face)**: Install a biomedical model like **BioBERT** for detecting drugs, diseases, etc.

### Task 3: Word Count & Tokenization
- **3.1**: Use a Python library to count the occurrences of words in the `.txt` file. Store the top 30 most common words and their counts in a CSV file.
- **3.2**: Write a function using the `AutoTokenizer` function from the Transformers library to count unique tokens in the text and list the top 30 words.

### Task 4: Named-Entity Recognition (NER)
- Extract 'diseases' and 'drugs' entities from the `.txt` file using:
  - **SpaCy (scispaCy)**: Use models like `en_core_sci_sm` and `en_ner_bc5cdr_md`.
  - **Transformers**: Use **BioBERT**.
- Compare the results of both models in terms of the total entities detected, most common words, and differences in detected entities.

---

## Question 2: The Quest for the Hidden Treasure

### Chapter 1: The Gatekeeper
- An algorithm generates a number `n`. Use this number to change the pixel values (r,g,b) in the provided image (`Chapter1.png`) by adding `n` to each pixel (i.e., (r+n, g+n, b+n)).
- Generate a new image with the updated pixels and save it as `chapter1out.png`.
- Sum all the red (r) pixel values in the new image and output the result to proceed to the next chapter.

### Chapter 2: The Chamber of Strings
- Solve various programming puzzles involving:
  - **Nested for loops**
  - **Conditional statements**
  - **String manipulations**
- Complete these challenges to reveal the final word that leads to the treasure.

---

## Question 3: Fixing Error-Prone Code

### Task 1: Reveal the Key
- Decrypt the provided encrypted code, which will reveal the key.

### Task 2: Write a Decryption Function
- Write the decryption function to decrypt the encrypted code into the original code.

### Task 3: Correct the Errors
- Correct the errors in the decrypted code.
- Provide comments in the code explaining each correction.

### Task 4: Program Output
- Ensure that the decrypted code, corrections, and comments are all shown in the program file.

---

## Question 4: GitHub Collaboration

### Task: Create a GitHub Repository
- Create a **public** GitHub repository and add all group members as collaborators.
- Track all contributions and code changes.
- Submit the GitHub repository link along with the final zipped files.


---
