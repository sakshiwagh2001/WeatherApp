# C:\Users\AGT25.DESKTOP-LKQKFEQ\Desktop\alpha\Django\weather_project\weather_data\serializers.py


from rest_framework import serializers
from .models import Region, Parameter, WeatherRecord

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = '__all__'

class WeatherRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherRecord
        fields = '__all__'