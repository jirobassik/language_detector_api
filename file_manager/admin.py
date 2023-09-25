from django.contrib import admin
from file_manager.models import FileModel

admin.site.register(FileModel)

# @admin.register(FileModel)
# class LessonStatusAdmin(admin.ModelAdmin):
#     list_display = ('upload_file', 'file_content',)
