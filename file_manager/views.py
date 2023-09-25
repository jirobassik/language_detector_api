import mimetypes
import os

from django.http import HttpResponse
from rest_framework import viewsets, views
from .models import FileModel
from .serializers import UploadedFileSerializer


class UploadedFileViewSet(viewsets.ModelViewSet):
    queryset = FileModel.objects.order_by('upload_file')
    serializer_class = UploadedFileSerializer
