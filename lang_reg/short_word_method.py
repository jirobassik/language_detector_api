from textmixin import TextMixin
from collections import Counter
from operator import ge, getitem
from decimal import Decimal


class ShortWord(TextMixin):
    __slots__ = (
        'filenames', 'short_english_words_probability', 'short_russian_words_probability')

    def __init__(self, *args):
        self.filenames = args
        self.short_english_words_probability = self.__create_poa('poa_files/test1.pdf')
        self.short_russian_words_probability = self.__create_poa('poa_files/test2.pdf')

    def short_method_analyze(self):
        res_dict_short_meth = {}
        for file in self.filenames:
            input_preprocess_text = self.remove_spaces_punctuation_short_meth(self.reading_txt_file(file))
            res_dict_short_meth[file] = self.__file_probability(input_preprocess_text)
        return res_dict_short_meth

    def __create_poa(self, filename: str):
        read_file_pdf_ = self.reading_pdf_file(filename)
        preprocess_pdf_text = self.remove_spaces_punctuation_short_meth(read_file_pdf_.lower())
        counter_words = Counter(preprocess_pdf_text)
        counter_num_short_words = self.__counter_number_short_words(counter_words)
        number_all_worlds = sum(counter_num_short_words.values())
        dict_probability_worlds = self.__calculate_probability_each_world(counter_num_short_words, number_all_worlds)
        return dict_probability_worlds

    def __file_probability(self, worlds: list):
        english_probability = self.__calculate_probability(worlds, self.short_english_words_probability)
        russian_probability = self.__calculate_probability(worlds, self.short_russian_words_probability)
        return {'english': english_probability, 'russian': russian_probability}

    @staticmethod
    def __counter_number_short_words(counter: dict):
        return dict(filter(lambda short_word: ge(getitem(short_word, 1), 3), counter.items()))

    @staticmethod
    def __calculate_probability_each_world(counter: dict, all_words_counter: int):
        return {short_word: num_short_word / all_words_counter for short_word, num_short_word in counter.items()}

    @staticmethod
    def __calculate_probability(text_words: list, counter_probability: dict):
        probability = Decimal(1.0)
        for word in text_words:
            if word.lower() in counter_probability.keys():
                probability *= Decimal(counter_probability.get(word, 0.01))
            else:
                probability *= Decimal(0.01)
        return probability


# short_word_meth = ShortWord('text1.txt', 'text2.txt')
# c = short_word_meth.short_method_analyze()
# print(c)
