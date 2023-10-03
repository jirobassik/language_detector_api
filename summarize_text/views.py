import time

from rest_framework.response import Response
from rest_framework.views import APIView
from file_manager.models import FileModel
from text_summarize.neuro_text_summarize import TextSummarize
from text_summarize.standart_text_summarize import StandartTextSummarize

summarize_text_ = TextSummarize()
standart_text_summarize = StandartTextSummarize()


class SummarizeTextAPIView(APIView):

    @staticmethod
    def get(request, pk):
        file_object = FileModel.objects.get(pk=pk)
        filename = file_object.upload_file.name
        start_time = time.time()
        sum_text = summarize_text_.summarize(filename)
        sum_text_standart = standart_text_summarize.summarize_text(filename)
        key_words = standart_text_summarize.summarize_keywords(filename)
        res_time = time.time() - start_time
        print(f'Затраченное время: {res_time}')
        return Response(
            {'sum_text': sum_text, 'sum_text_standart': sum_text_standart, 'key_words': key_words, 'filename': filename,
             'file_id': pk})
