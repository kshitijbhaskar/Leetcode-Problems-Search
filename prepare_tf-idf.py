from sklearn.feature_extraction.text import TfidfVectorizer
from preprocess import preprocess_text

# Read the index file
index_file = 'preprocessed_output.txt'
with open(index_file, 'r', encoding='latin-1') as file:
    questions = file.readlines()

# Take search query as user input
search_query = input("Enter your search query: ")

# Preprocess the search query using the same preprocessing steps as before
search_query = preprocess_text(search_query)

# Preprocess the questions and create a corpus
corpus = []
for question in questions:
    preprocessed_question = preprocess_text(question)
    corpus.append(preprocessed_question)

# Create the TF-IDF vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

# Transform the search query into a TF-IDF vector
query_vector = vectorizer.transform([search_query])

# Compute the cosine similarity between the query vector and the TF-IDF matrix
cosine_similarities = tfidf_matrix.dot(query_vector.T).toarray().flatten()

# Create a list of (line_number, question, cosine similarity) tuples for relevant results
results = [(line_number, question, similarity) for line_number, question, similarity in zip(range(1, len(questions) + 1), questions, cosine_similarities) if similarity > 0]

# Sort the results based on the cosine similarity (in descending order)
results.sort(key=lambda x: x[2], reverse=True)

def print_line(file_path, line_number):
    with open(file_path, 'r', encoding='latin-1') as file:
        lines = file.readlines()
        if 1 <= line_number <= len(lines):
            line = lines[line_number - 1]
            print(f"Index no. {line_number}. Question no. {line.strip()}")

file_path = 'index.txt'

# Print the ranked questions with their line numbers
for line_number, question, similarity in results:
    print_line(file_path, line_number)
