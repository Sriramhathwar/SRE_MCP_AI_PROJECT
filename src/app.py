from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from main import handle_query

app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    query = request.json["query"]
    answer = handle_query(query)
    return jsonify({"answer": answer})

app.run(debug=True)