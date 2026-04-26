import pytesseract
from pdf2image import convert_from_path
import re
def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)
    return text
def validate_entities(entities):
    validated = []

    for ent in entities:
        label = ent['label']
        value = ent['text']
        if label == "DATE":
            if re.match(r"\d{4}-\d{2}-\d{2}", value):
                validated.append(ent)

        elif label == "MONEY":
            if re.search(r"\$|₹|€", value):
                validated.append(ent)

        else:
            validated.append(ent)
