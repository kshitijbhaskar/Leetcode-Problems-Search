# Leetcode Problems Search

Leetcode Problems Search is a web application that allows users to search for Leetcode questions based on their queries. The application uses TF-IDF vectorization and cosine similarity to match search queries with relevant Leetcode questions.

## Demo

You can access the live demo of the application [here](https://leetcode-problems-search.onrender.com). Feel free to visit the site and try out the search functionality.

<img width="960" alt="image" src="https://github.com/kshitijbhaskar/leetcode-questions-search/assets/95466193/5aeb8c19-2b08-4995-a810-b28cb8893ef9">

## Features

- Search for Leetcode questions using keywords or phrases.
- View search results with relevant question titles, descriptions, and links.
- Preview question functionality to quickly view question details without opening in a new tab.
- Pagination support for easy navigation through search results.
- Dark theme toggle for a personalized user experience.

## Implementation Details

The Leetcode Problems Search project is implemented using Python, Flask, and scikit-learn library for TF-IDF vectorization. Here's an overview of the project's structure:

- `app.py`: This file contains the Flask application code that sets up the routes, and handles the search queries.
- `results.html`: This HTML template is used to display the search results, including the question titles, descriptions, and pagination.
- `index.html`: This HTML template renders the homepage with the search bar and navigation elements.
- `templates/`: This directory contains the HTML templates used by Flask for rendering the web pages.
- `static/`: This directory includes static files such as CSS stylesheets (`style.css`) and JavaScript files (`script.js`).
- `preprocess.py`: This module provides functions for preprocessing text data, used for both indexing and search query processing.
- `preprocessed_output.txt`: This file contains the preprocessed Leetcode question data.
- `index.txt`: This file contains the question titles used for displaying search results.
- `Qindex.txt`: This file contains the question links used for linking to the Leetcode website.
- `q-data/`: This directory stores the question descriptions, each in a separate text file named by question number.

## Hosting

The Leetcode Problems Search application is currently hosted on [Render](https://render.com). You can access it at [https://leetcode-problems-search.onrender.com](https://leetcode-problems-search.onrender.com).
