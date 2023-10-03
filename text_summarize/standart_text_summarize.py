import pprint
from math import log
from operator import getitem
from nltk import sent_tokenize
from rake_nltk import Rake

from text_summarize.textmixin import TextMixin


class StandartTextSummarize(TextMixin):
    __slots__ = ('rake',)

    def __init__(self):
        self.rake = Rake()

    def summarize_keywords(self, filename: str):
        text = self.reading_pdf_file('media', filename).replace('\n', '')
        self.rake.extract_keywords_from_text(text)
        return ', '.join(self.rake.get_ranked_phrases()[:5])

    def summarize_text(self, filename: str):
        text_without_n = self.reading_pdf_file('media', filename).replace('\n', '')
        list_sentence_tokenize = sent_tokenize(text_without_n)
        scores = self.calculate_weight_sentences(text_without_n, list_sentence_tokenize)
        sentence_score = zip(list_sentence_tokenize, scores)
        sorted_sentence_score = dict(sorted(sentence_score, key=lambda item: getitem(item, 1), reverse=True))
        return ' '.join(list(sorted_sentence_score.keys())[:10])

    def calculate_weight_sentences(self, text: str, sent_tokenize_: list):
        list_words, list_sentences = self.tokenize_text(text), list(map(self.tokenize_text, sent_tokenize_))
        scores = []
        for sentences in list_sentences:
            score = 0
            for word in sentences:
                score += self.__term_frequency(sentences, word) * \
                         self.__inverse_document_frequency(word, list_words, list_sentences)
            scores.append(score)
        return scores

    @staticmethod
    def __term_frequency(sentence: list, word: str):
        try:
            term_freq = sentence.count(word) / len(sentence)
        except ZeroDivisionError:
            term_freq = 0.000001
        return term_freq

    def __inverse_document_frequency(self, word: str, list_words: list, list_sentences: list):
        return 0.5 * (1 + self.__term_frequency(list_words, word) / self.__max_frequency(list_sentences, word)) * \
            log(len(list_sentences) / 1)  # Что делать с еденицией

    def __max_frequency(self, list_sentences: list, word: str):
        term_frequency = 0
        for sentence in list_sentences:
            if term_frequency < (new_term_freq := self.__term_frequency(sentence, word)):
                term_frequency = new_term_freq
        return term_frequency
