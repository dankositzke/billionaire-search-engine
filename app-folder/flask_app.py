from elasticsearch import Elasticsearch
from flask import Flask, render_template, url_for, request, redirect
from pytz import timezone
from flask.wrappers import Request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Elastic search code... I'll fit this into the appropriate spots at the end
client = Elasticsearch(
    cloud_id="Billionaire_Search_Engine:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJDI5MDUyYzllMTM4MDRhZDhhZjRiNWFiNjgzYzE0OGYxJDUzYjE2ZWNmMGIyYjRjNTJhNzZjZDc2ZjU4ZWViNDI2",
    http_auth=("elastic", "HmFjxrUrt4SIxfUya6ig5nzZ"),
)

# Set up Flask app
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        user_search_term = request.form["search_content"]
        query = {"query": {"match": {"text": {"query": str(user_search_term)}}}}
        query_results = client.search(
            index="ts_transcript_title_url_billionaire", body=query
        )
        query_results = query_results["hits"]["hits"]
        return render_template("searchresults.html", query_results=query_results)
    else:
        return render_template("index.html")


@app.route("/searchresults")
def searchresults():
    return render_template("searchresults.html")


if __name__ == "__main__":
    app.run(debug=True)
