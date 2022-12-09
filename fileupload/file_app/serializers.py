from rest_framework import serializers
from .models import File, TenderImport

class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = File
    fields = ('file','timestamp')

class TenderSerializer(serializers.ModelSerializer):
  class Meta():
    model = TenderImport
    fields = "__all__"