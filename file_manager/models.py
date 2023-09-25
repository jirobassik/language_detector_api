import pathlib
from django.db import models
from utils.read_pdf import read_one_page_pdf


class FileModel(models.Model):
    upload_file = models.FileField("File", unique=True, )
    file_content = models.CharField(null=True, editable=False, max_length=10000)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.upload_file:
            self.file_content = read_one_page_pdf(self.upload_file.name)[1:40]

    def delete(self, using=None, keep_parents=False):
        pathlib.Path('media', self.upload_file.name).unlink(missing_ok=False)
        super().delete()

    def __str__(self):
        return self.upload_file.name
