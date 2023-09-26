from rest_framework import serializers
from .models import FileModel


class UploadedFileSerializer(serializers.ModelSerializer):
    file_content = serializers.CharField

    class Meta:
        model = FileModel
        fields = ('id', 'upload_file', 'file_content')
