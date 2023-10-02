from text_summarize.textmixin import TextMixin
from summarizer.sbert import SBertSummarizer


class TextSummarize(TextMixin):
    __slots__ = ('model', )

    def __init__(self):
        self.model = SBertSummarizer('paraphrase-MiniLM-L6-v2')

    def summarize(self, filename: str):
        text = self.reading_pdf_file('media', filename)
        return self.model(text, num_sentences=5)
