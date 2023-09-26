import pathlib
from django.db import models
from utils.read_pdf import read_one_page_pdf


class FileModel(models.Model):
    upload_file = models.FileField("File", unique=True, )

    @property
    def file_content(self):
        return read_one_page_pdf(self.upload_file.name)[0:70]

    def delete(self, using=None, keep_parents=False):
        pathlib.Path('media', self.upload_file.name).unlink(missing_ok=False)
        super().delete()

    def __str__(self):
        return self.upload_file.name
