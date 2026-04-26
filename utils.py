import pytesseract
from pdf2image import convert_from_path
import re
def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""