import time
from collections import Counter
from string import ascii_letters
from itertools import chain
from lang_reg.textmixin import TextMixin


class Alphabets:
    __slots__ = ('english_letters', 'russian_letters')

    def __init__(self):
        self.english_letters = ascii_letters
        self.russian_letters = self.__russian_letters_def()

    @staticmethod
    def __russian_letters_def() -> str:
        start_unicode_point_rus = ord('а')
        lower_rus_letters = ''.join(
            chain([chr(unicode_alph) for unicode_alph in range(start_unicode_point_rus, start_unicode_point_rus + 6)],
                  [chr(start_unicode_point_rus + 33)],
                  [chr(unicode_alph) for unicode_alph in
                   range(start_unicode_point_rus + 6, start_unicode_point_rus + 32)]))
        upper_rus_letters = lower_rus_letters.upper()
        return lower_rus_letters + upper_rus_letters


class AlphabetMethod(Alphabets, TextMixin):

    def __init__(self):
        super().__init__()

    def __count_letters(self, file_name):
        text_counter = Counter(self.remove_spaces_punctuation(self.reading_pdf_file('media', file_name)))
        return text_counter, text_counter.total()

    def alphabet_method_many_files(self, *args):
        dict_percent_files = {}
        start_time = time.time()
        for filename in args:
            engl_percent, rus_percent = self.__letter_percent(filename)
            dict_percent_files[filename] = 'english' if engl_percent > rus_percent else 'russian'
        res_time = time.time() - start_time
        return dict_percent_files, res_time

    def alphabet_method_one_file(self, filename: str):
        engl_percent, rus_percent = self.__letter_percent(filename)
        percent_dict = {'english_percent': engl_percent, 'russian_percent': rus_percent}
        return 'english' if percent_dict['english_percent'] > percent_dict['russian_percent'] else 'russian'

    def __letter_percent(self, filename: str):
        alph_counter, all_alphs = self.__count_letters(filename)
        engl_percent = self.__calculate_alph_percents(self.english_letters, alph_counter, all_alphs)
        rus_percent = self.__calculate_alph_percents(self.russian_letters, alph_counter, all_alphs)
        return engl_percent, rus_percent

    @staticmethod
    def __calculate_alph_percents(letters: str, alph_counter: Counter, all_alphs: int):
        return sum(((alph_counter.get(alph, 0) / all_alphs) * 100 for alph in letters))
