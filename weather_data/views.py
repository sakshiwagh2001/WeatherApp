

# C:\Users\saksh\Desktop\Weather App\weather_project\weather_data\views.py


# weather_data/views.py

from rest_framework import viewsets, filters
from .models import WeatherRecord, Region, Parameter
from .serializers import WeatherRecordSerializer, RegionSerializer, ParameterSerializer
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from utils.file_generator import generate_weather_txt
from django.http import HttpResponse

class WeatherRecordViewSet(viewsets.ModelViewSet):
    queryset = WeatherRecord.objects.all()
    serializer_class = WeatherRecordSerializer

    # ✅ Filtering by URL /api/weather/?parameter__name=Tmax&year=2023
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['region__name', 'parameter__name', 'year']  
    ordering_fields = ['year']

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class ParameterViewSet(viewsets.ModelViewSet):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer

def weather_table_view(request):
    regions = Region.objects.values_list('name', flat=True)
    parameters = Parameter.objects.values_list('name', flat=True)

    selected_region = request.GET.get('region')
    selected_parameter = request.GET.get('parameter')

    records = WeatherRecord.objects.all()

    if selected_region:
        records = records.filter(region__name=selected_region)
    if selected_parameter:
        records = records.filter(parameter__name=selected_parameter)

    if request.GET.get('download') == 'true':
        txt_content = generate_weather_txt(records)
        response = HttpResponse(txt_content, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="weather_data.txt"'
        return response

    context = {
        'regions': regions,
        'parameters': parameters,
        'records': records,
        'selected_region': selected_region,
        'selected_parameter': selected_parameter,
    }
    return render(request, 'weather_data/weather_list.html', context)
