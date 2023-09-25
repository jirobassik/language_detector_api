from lang_reg.textmixin import TextMixin
from langid.langid import LanguageIdentifier, model


class Neuro(TextMixin):
    __slots__ = ('filenames',)

    def __init__(self, *args):
        self.filenames = args

    def neuro_method(self):
        dict_neuro_res = {}
        for file in self.filenames:
            dict_neuro_res[file] = self.__langid_identifier(self.reading_txt_file(file))
        return dict_neuro_res

    @staticmethod
    def __langid_identifier(text: str):
        identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
        return identifier.classify(text)


# a = Neuro('text1.txt', 'text4.txt')
# print(a.neuro_method())
