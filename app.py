
from flask import Flask, request, jsonify
import os

from utils import extract_text_from_pdf, validate_entities
from ner_model import extract_entities

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return {"message": "LexiScan Auto API Running 🚀"}


@app.route("/process", methods=["POST"])
def process_document():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    text = extract_text_from_pdf(file_path)
    entities = extract_entities(text)
    validated_entities = validate_entities(entities)

    return jsonify({
        "text_sample": text[:1000],
        "entities": validated_entities
    })


if __name__ == "__main__":
    app.run(debug=True)