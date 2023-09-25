from rest_framework.response import Response
from rest_framework.views import APIView
from file_manager.models import FileModel
from lang_reg.alhpabet_method import AlphabetMethod
from lang_reg.short_word_method import ShortWord
from lang_reg.neuro_method import Neuro

alphabet_method = AlphabetMethod()
short_word_method = ShortWord()
neuro_method = Neuro()

class AlphabetDetectorLanguageAPIView(APIView):

    @staticmethod
    def get(request, pk):
        file_object = FileModel.objects.get(pk=pk)
        filename = file_object.upload_file.name
        return Response({'text_language': alphabet_method.alphabet_method_one_file(filename), 'filename': filename})


class ShortWordDetectorLanguageAPIView(APIView):

    @staticmethod
    def get(request, pk):
        file_object = FileModel.objects.get(pk=pk)
        filename = file_object.upload_file.name
        return Response(
            {'text_language': short_word_method.short_method_analyze_one_file(filename), 'filename': filename})


class NeuroDetectorLanguageAPIView(APIView):

    @staticmethod
    def get(request, pk):
        file_object = FileModel.objects.get(pk=pk)
        filename = file_object.upload_file.name
        return Response(
            {'text_language': neuro_method.neuro_method_one_file(filename), 'filename': filename})
