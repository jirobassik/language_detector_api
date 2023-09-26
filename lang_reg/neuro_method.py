import time

from lang_reg.textmixin import TextMixin
from langid.langid import LanguageIdentifier, model


class Neuro(TextMixin):

    def neuro_method_many_files(self, *args):
        dict_neuro_res = {}
        start_time = time.time()
        for file in args:
            dict_languages = {'en': 'english', 'ru': 'russian'}
            dict_language = self.__langid_identifier(self.reading_pdf_file('media', file))
            dict_neuro_res[file] = dict_languages.get(dict_language[0], 'unknown')
        res_time = time.time() - start_time
        return dict_neuro_res, res_time

    def neuro_method_one_file(self, file_name):
        dict_language = {'en': 'english', 'ru': 'russian'}
        dict_neuro_res = self.__langid_identifier(self.reading_pdf_file('media', file_name))
        return dict_language.get(dict_neuro_res[0], 'unknown')

    @staticmethod
    def __langid_identifier(text: str):
        identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
        return identifier.classify(text)
