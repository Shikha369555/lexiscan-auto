# 📄 LexiScan Auto - Intelligent Document Processing System

LexiScan Auto is an AI-powered document processing system that extracts text from PDF documents using OCR and identifies important entities using Natural Language Processing (NLP).

---

## 🚀 Features

- 📤 Upload PDF documents
- 🔍 OCR-based text extraction using Tesseract
- 🧠 Named Entity Recognition (NER) using spaCy
- ✅ Entity validation using rule-based processing
- 📊 Interactive Streamlit Dashboard
- ⚡ Flask REST API Backend
- 📑 Extract Dates, Organizations, Persons, Locations, Money, and more

---

## 🏗️ System Architecture

PDF Upload
↓
OCR (Tesseract)
↓
Text Extraction
↓
spaCy NER Model
↓
Entity Validation
↓
Structured Output

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Flask

### OCR
- Tesseract OCR

### NLP
- spaCy
- en_core_web_sm Model

### PDF Processing
- pdf2image
- Pillow

### Language
- Python

---

## 📂 Project Structure

```text
lexiscan-auto/
│
├── app.py
├── streamlit_app.py
├── utils.py
├── ner_model.py
├── requirements.txt
├── uploads/
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/lexiscan-auto.git
cd lexiscan-auto
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4: Install spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

## 🔧 External Dependencies

### Install Tesseract OCR

Download and Install:

https://github.com/UB-Mannheim/tesseract/wiki

Verify Installation:

```bash
tesseract --version
```

---

### Install Poppler

Download:

https://github.com/oschwartz10612/poppler-windows/releases/

Extract to:

```text
C:\poppler
```

Update path inside `utils.py`:

```python
POPPLER_PATH = r"C:\poppler\poppler-26.02.0\Library\bin"
```

---

## ▶️ Running the Application

### Terminal 1 (Flask Backend)

```bash
python app.py
```

Expected Output:

```text
Running on http://127.0.0.1:5000
```

---

### Terminal 2 (Streamlit Dashboard)

```bash
streamlit run streamlit_app.py
```

---

## 📸 Application Workflow

1. Upload PDF Document
2. Convert PDF Pages to Images
3. Extract Text Using OCR
4. Detect Entities Using spaCy
5. Validate Extracted Entities
6. Display Results on Dashboard

---

## 📊 Sample Extracted Entities

| Entity | Label |
|----------|----------|
| John Doe | PERSON |
| Microsoft | ORG |
| New York | GPE |
| ₹50,000 | MONEY |
| 2025-01-01 | DATE |

---

## 🎯 Use Cases

- Legal Contract Analysis
- Agreement Processing
- Invoice Data Extraction
- Compliance Verification
- Document Digitization

---

## 🔮 Future Enhancements

- Multi-language OCR
- PDF Summarization
- AI-based Risk Analysis
- Clause Detection
- Database Integration
- Cloud Deployment

---

## 👨‍💻 Author

Shikha Singh

### Skills

- Python Development
- Machine Learning
- Natural Language Processing
- Full Stack Development
- AI Applications

---

## 📜 License

This project is developed for educational and learning purposes.

-----------
