import PyPDF2
from pathlib import Path

def read_one_page_pdf(filename: str):
    with open(Path('media', filename), 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        page = reader.pages[0]
        return page.extract_text()
