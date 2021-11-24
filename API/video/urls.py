from django.contrib import admin
from django.urls import path
from .views import ListVideo
urlpatterns = [
    path(r'videos/', ListVideo.as_view(), name="lista-video"),
]
