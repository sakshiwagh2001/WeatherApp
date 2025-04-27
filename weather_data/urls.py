

# C:\Users\saksh\Desktop\Weather App\weather_project\weather_data\urls.py

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import WeatherRecordViewSet, RegionViewSet, ParameterViewSet, weather_table_view

router = DefaultRouter()
router.register(r'weather', WeatherRecordViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'parameters', ParameterViewSet)

urlpatterns = router.urls

