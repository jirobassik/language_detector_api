# language_detector_api
## Run
```python manage.py runserver localhost:8001```
## Has the following functionality:
- Add, delete files (localhost:8001/api/v1/uploadfiles)
- Download file (localhost:8001/api/v1/download/<int:id>)
- Detect language (alphabet method) (localhost:8001/api/v1/alphabet/<int:pk>)
- Detect language (shord word method) (localhost:8001/api/v1/short/<int:pk>)
- Detect language (neuro method) (localhost:8001/api/v1/neuro/<int:pk>)
- Generate statistic, all files (localhost:8001/api/v1/files_statistic/)

## Works in conjunction with https://github.com/jirobassik/language_detector_client
