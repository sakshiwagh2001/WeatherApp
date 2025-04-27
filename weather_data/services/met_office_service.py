# C:\Users\AGT25.DESKTOP-LKQKFEQ\Desktop\alpha\Django\weather_project\weather_data\services\met_office_service.py

import requests
from .base_weather_service import BaseWeatherService

class MetOfficeService(BaseWeatherService):
    def fetch_weather_data(self, region_name, parameter_name,backfill=False):
        url = f"https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{parameter_name}/date/{region_name}.txt"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch data: {e}")