import time

from rest_framework.response import Response
from rest_framework.views import APIView
from file_manager.models import FileModel
from text_summarize.text_summarize import TextSummarize

summarize_text_ = TextSummarize()


class SummarizeTextAPIView(APIView):

    @staticmethod
    def get(request, pk):
        file_object = FileModel.objects.get(pk=pk)
        filename = file_object.upload_file.name
        start_time = time.time()
        sum_text = summarize_text_.summarize(filename)
        res_time = time.time() - start_time
        print(f'Затраченное время: {res_time}')
        return Response({'sum_text': sum_text, 'filename': filename, 'file_id': pk})
