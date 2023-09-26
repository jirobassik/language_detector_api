import mimetypes
import os

from django.http import HttpResponse
from rest_framework import viewsets, views
from .models import FileModel
from .serializers import UploadedFileSerializer

class UploadedFileViewSet(viewsets.ModelViewSet):
    queryset = FileModel.objects.order_by('upload_file')
    serializer_class = UploadedFileSerializer


class DownloadFileViewSet(views.APIView):

    @staticmethod
    def get(request, id):
        file_object = FileModel.objects.get(pk=id)
        filename = file_object.upload_file.name
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_location = base_dir + f'/media/{filename}'
        file_data = open(file_location, 'rb')
        mime_type, _ = mimetypes.guess_type(file_location)
        response = HttpResponse(file_data, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response
