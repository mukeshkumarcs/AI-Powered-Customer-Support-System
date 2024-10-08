from flask import Flask, request, jsonify
from google.cloud import aiplatform
from transformers import pipeline

app = Flask(__name__)

# Load a pre-trained Large Language Model (LLM) for customer queries
qa_pipeline = pipeline("question-answering")

# Function to handle customer queries using LLM
@app.route("/api/query", methods=["POST"])
def handle_query():
    data = request.json
    question = data.get('question', '')

    if not question:
        return jsonify({"error": "No question provided"}), 400

    context = "This is a demo context for answering customer support queries."  # You can replace with actual context or knowledge base
    response = qa_pipeline(question=question, context=context)

    return jsonify({
        "question": question,
        "answer": response['answer']
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
