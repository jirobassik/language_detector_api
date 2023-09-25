from lang_reg.textmixin import TextMixin
from langid.langid import LanguageIdentifier, model


class Neuro(TextMixin):

    def neuro_method_many_files(self, *args):
        dict_neuro_res = {}
        for file in args:
            dict_neuro_res[file] = self.__langid_identifier(self.reading_pdf_file('media', file))
        return dict_neuro_res

    def neuro_method_one_file(self, file_name):
        dict_neuro_res = self.__langid_identifier(self.reading_pdf_file('media', file_name))
        return dict_neuro_res

    @staticmethod
    def __langid_identifier(text: str):
        identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
        return identifier.classify(text)
