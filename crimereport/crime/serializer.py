from .models import Congressperson
from rest_framework import serializers

class CongresspersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Congressperson #Congressperson 모델을 기반으로 serialize
        fields = '__all__'