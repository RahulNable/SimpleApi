from django.conf.urls import url
from .views import FileView, extractFile, getFileNames

urlpatterns = [
    url(r'^upload/$', FileView.as_view(), name='file-upload'),
    url(r'^data/$', extractFile, name='extract'),
    url(r'^filelist/$', getFileNames, name='filelist'),
]