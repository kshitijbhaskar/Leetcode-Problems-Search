import os
import codecs
import linecache
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from preprocess import preprocess_text

app = Flask(__name__)

# Read lines from a file
def read_lines(file_path, start_line, num_lines):
    lines = []
    for line_number in range(start_line, start_line + num_lines):
        line = linecache.getline(file_path, line_number).strip()
        if line:
            lines.append(line)
    return lines[0] if lines else ""

# Read the index file
index_file = 'preprocessed_output.txt'
with open(index_file, 'r', encoding='latin-1') as file:
    questions = file.readlines()

# Preprocess the questions and create a corpus
corpus = []
for question in questions:
    preprocessed_question = preprocess_text(question)
    corpus.append(preprocessed_question)

# Create the TF-IDF vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['query']

    # Preprocess the search query using the same preprocessing steps as before
    search_query = preprocess_text(search_query)

    # Transform the search query into a TF-IDF vector
    query_vector = vectorizer.transform([search_query])

    # Compute the cosine similarity between the query vector and the TF-IDF matrix
    cosine_similarities = tfidf_matrix.dot(query_vector.T).toarray().flatten()

    # Create a list of (line_number, question, cosine similarity) tuples for relevant results
    results = [(line_number, question, similarity) for line_number, question, similarity in zip(range(1, len(questions) + 1), questions, cosine_similarities) if similarity > 0]


    # Sort the results based on the cosine similarity (in descending order)
    results.sort(key=lambda x: x[2], reverse=True)

    results_list = []
    for line_number, _, _ in results:
        # Read the question number and title
        with open('index.txt', 'r', encoding='latin-1') as file:
            lines = file.readlines()
        question_title = lines[line_number - 1].strip()
        # Read the question link
        question_link = linecache.getline('Qindex.txt', line_number).strip()
        # Find the corresponding folder path and description file
        folder_path = os.path.join('q-data', str(line_number))
        description_file = os.path.join(folder_path, f"{line_number}.txt")
        # Read question description
        q_description = read_lines(description_file, 0, 5)
        results_list.append((question_link, question_title, q_description))

    return render_template('results.html', query=search_query, results=results_list)


if __name__ == '__main__':
    app.run()
