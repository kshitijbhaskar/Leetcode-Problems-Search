import os
import linecache
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from preprocess import preprocess_text

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.urandom(24)

# Read lines from a file
def read_lines(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        return file.read()

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

@app.route('/search', methods=['GET', 'POST'])
def search():
    search_query = request.args.get('query', '') if request.method == 'GET' else request.form['query']
    page = int(request.args.get('page', 1))

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

    # Pagination
    results_per_page = 10
    total_results = len(results)
    total_pages = (total_results + results_per_page - 1) // results_per_page
    start_idx = (page - 1) * results_per_page
    end_idx = start_idx + results_per_page
    paginated_results = results[start_idx:end_idx]

    results_list = []
    for line_number, _, _ in paginated_results:
        # Read the question number and title
        with open('index.txt', 'r', encoding='latin-1') as file:
            lines = file.readlines()
        question_title = lines[line_number - 1].strip()
        # Read the question link
        question_link = linecache.getline('Qindex.txt', line_number).strip()
        # Find the corresponding folder path and description file
        folder_path = os.path.join('q-data', str(line_number))
        description_file = os.path.join(folder_path, f"{line_number}.txt")
        # Read the complete question description
        with open(description_file, 'r', encoding='latin-1') as desc_file:
            q_description = desc_file.read()
        results_list.append((question_link, question_title, q_description))

    # Pagination - Calculate start_page and end_page
    max_visible_pages = 5  # Maximum number of visible page links
    start_page = max(1, page - max_visible_pages // 2)
    end_page = start_page + max_visible_pages - 1
    if end_page > total_pages:
        end_page = total_pages

    return render_template('results.html', query=search_query, results=results_list, page=page, total_pages=total_pages, start_page=start_page, end_page=end_page)

if __name__ == '__main__':
    app.run(debug=True)
