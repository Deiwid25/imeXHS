from rest_framework import serializers
from .models import Element

class ElementSerializer(serializers.ModelSerializer):
  class Meta:
    model = Element
    fields = '__all__'


class ElementUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Element
    fields = ['id','device_name']

class ElementGetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Element
    fields = ['device_name','average_before_normalization','average_after_normalization','data_size','raw_data']