# Import Flask framework components
from flask import Flask, request, render_template

# Import the semantic search App class (CLIP + FAISS logic)
from app import App

# Create Flask application instance
flask_app = Flask(__name__)

# Renders the search UI (index.html)
@flask_app.route("/")
def index():
    return render_template("index.html")

# Route for handling search requests
@flask_app.route("/search")
def search():
    search_query = request.args.get("search_query")

    app = App()
    results = app.search(search_query, results=5)
    return results

# Run Flask application
if __name__ == "__main__":
    flask_app.run(port=5000)
