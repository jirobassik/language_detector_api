import time

from lang_reg.textmixin import TextMixin
import fasttext


class Neuro(TextMixin):
    __slots__ = ('dict_language', 'model',)

    def __init__(self):
        self.dict_language = {'en': 'english', 'ru': 'russian'}
        self.model = fasttext.load_model('D:\Programs\PyCharm 2021.3.3\lnaguage_detector_api\lid.176.ftz')

    def neuro_method_many_files(self, *args):
        dict_neuro_res = {}
        start_time = time.time()
        for file in args:
            tuple_language = self.__langid_identifier(self.reading_pdf_file('media', file))
            dict_neuro_res[file] = self.dict_language.get(tuple_language[0], 'unknown')
        res_time = time.time() - start_time
        return dict_neuro_res, res_time

    def neuro_method_one_file(self, file_name):
        dict_neuro_res = self.__langid_identifier(self.reading_pdf_file('media', file_name))
        return self.dict_language.get(dict_neuro_res[0], 'unknown'), dict_neuro_res[1]

    def __langid_identifier(self, text: str):
        text_without_newlines = text.replace('\n', '')
        result = self.model.predict(text_without_newlines)
        language = result[0][0].split("__")[-1]
        return language, 1.0
