import string
import re

# Define the path to the output file
output_file = 'output.txt'

# Define the path to store the preprocessed output
preprocessed_file = 'preprocessed_output.txt'

# Define a list of stopwords
stop_words = [
    'a', 'an', 'the', 'in', 'on', 'at', 'to', 'for', 'of', 'by', 'with', 'is', 'are',
    'was', 'were', 'am', 'is', 'are', 'i', 'you', 'he', 'she', 'it', 'we', 'they'
]

def preprocess_text(text):
    # Remove extra numbers, symbols, and spaces
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'[^\w\s]', '', text)  # Remove symbols
    text = ' '.join(text.split())  # Remove extra spaces

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text
    tokens = text.lower().split()

    # Remove stopwords and perform lemmatization
    preprocessed_tokens = [token for token in tokens if token not in stop_words]
    preprocessed_tokens = [token.strip() for token in preprocessed_tokens]

    # Remove single letters
    preprocessed_tokens = [token for token in preprocessed_tokens if len(token) > 1]

    # Replace or ignore problematic characters
    preprocessed_line = ' '.join(preprocessed_tokens)
    preprocessed_line = preprocessed_line.encode('ascii', 'ignore').decode('ascii')

    return preprocessed_line


# Preprocess the output file
with open(output_file, 'r', encoding='latin-1', errors='ignore') as file:
    lines = file.readlines()

    preprocessed_lines = []
    for line in lines:
        preprocessed_line = preprocess_text(line)
        if preprocessed_line:
            preprocessed_lines.append(preprocessed_line + '\n')

# Write the preprocessed lines to a new file
with open(preprocessed_file, 'w', encoding='latin-1') as file:
    file.writelines(preprocessed_lines)

print(f"Preprocessed lines have been written to {preprocessed_file}.")
