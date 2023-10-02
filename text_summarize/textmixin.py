from pathlib import Path
from string import punctuation

from nltk import word_tokenize
import PyPDF2


class TextMixin:

    @staticmethod
    def reading_txt_file(filename: str):
        return Path("../media", filename).read_text('utf-8')

    @staticmethod
    def reading_pdf_file(folder_name: str, filename: str):
        text = ""
        with open(Path(folder_name, filename), 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text += page.extract_text()
        return text

    @staticmethod
    def remove_spaces_punctuation(text):
        tokens = word_tokenize(text)
        table = str.maketrans('', '', punctuation)
        tokens = [word.translate(table) for word in tokens if word not in punctuation]
        cleaned_text = ''.join(tokens)
        return cleaned_text

    @staticmethod
    def remove_spaces_punctuation_short_meth(text: str, world_len=3):
        tokens = word_tokenize(text)
        table = str.maketrans('', '', punctuation)
        tokens = [word.translate(table).lower() for word in tokens if
                  word not in punctuation and len(word) <= world_len]
        return tokens
