from rest_framework.response import Response
from rest_framework.views import APIView
from file_manager.models import FileModel
from lang_reg.alhpabet_method import AlphabetMethod
from lang_reg.short_word_method import ShortWord
from lang_reg.neuro_method import Neuro
from utils.statistic_file import calculate_statistic_file

alphabet_method = AlphabetMethod()
short_word_method = ShortWord()
neuro_method = Neuro()


class AlphabetDetectorLanguageAPIView(APIView):

    @staticmethod
    def get(request, pk):
        file_object = FileModel.objects.get(pk=pk)
        filename = file_object.upload_file.name
        return Response(
            {'text_language': alphabet_method.alphabet_method_one_file(filename), 'filename': filename, 'file_id': pk})


class ShortWordDetectorLanguageAPIView(APIView):

    @staticmethod
    def get(request, pk):
        file_object = FileModel.objects.get(pk=pk)
        filename = file_object.upload_file.name
        return Response(
            {'text_language': short_word_method.short_method_analyze_one_file(filename), 'filename': filename,
             'file_id': pk})


class NeuroDetectorLanguageAPIView(APIView):

    @staticmethod
    def get(request, pk):
        file_object = FileModel.objects.get(pk=pk)
        filename = file_object.upload_file.name
        return Response(
            {'text_language': neuro_method.neuro_method_one_file(filename), 'filename': filename, 'file_id': pk})


class FileStatisticAPIView(APIView):

    @staticmethod
    def get(request):
        file_list = list(FileModel.objects.values_list('upload_file', flat=True))
        alphabet_result, alphabet_time = alphabet_method.alphabet_method_many_files(*file_list)
        short_result, short_time = short_word_method.short_method_analyze_many_files(*file_list)
        neuro_result, neuro_time = neuro_method.neuro_method_many_files(*file_list)
        english_percent, russian_percent = calculate_statistic_file(file_list, alphabet_result)
        return Response(
            {'alphabet_time': alphabet_time, 'short_time': short_time, 'neuro_time': neuro_time,
             'english_percent': english_percent, 'russian_percent': russian_percent})
