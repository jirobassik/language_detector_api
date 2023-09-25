"""
URL configuration for lnaguage_detector_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from file_manager.views import UploadedFileViewSet
from lang_detector.views import AlphabetDetectorLanguageAPIView

router = routers.SimpleRouter()
router.register(r'api/v1/uploadfiles', UploadedFileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/alphabet/<int:pk>', AlphabetDetectorLanguageAPIView.as_view()),
    path('', include(router.urls)),
]
