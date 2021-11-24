from django.contrib import admin
from .views import ListVideo
from django.conf.urls import url
urlpatterns = [
    url(r'^videos/$', ListVideo.as_view(), name="lista-video"),
]
