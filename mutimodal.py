import fitz
import pytesseract
from PIL import Image

# tell pytesseract where tesseract is installed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        # open pdf and extract text from all pages
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    elif file_path.endswith(('.png', '.jpg', '.jpeg')):
        # open image and extract text using OCR
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)
        return text

    return ""