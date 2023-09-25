from rest_framework.response import Response
from rest_framework.views import APIView
from file_manager.models import FileModel
from lang_reg.alhpabet_method import AlphabetMethod

alphabet_method = AlphabetMethod()

class AlphabetDetectorLanguageAPIView(APIView):

    @staticmethod
    def get(request, pk):
        file_object = FileModel.objects.get(pk=pk)
        filename = file_object.upload_file.name
        return Response({'text_language': alphabet_method.alphabet_method_one_file(filename), 'filename': filename})
