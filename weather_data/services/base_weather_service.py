# C:\Users\AGT25.DESKTOP-LKQKFEQ\Desktop\alpha\Django\weather_project\weather_data\services\base_weather_service.py

class BaseWeatherService:
    def fetch_weather_data(self, region_name, parameter_name):
        raise NotImplementedError("Subclasses should implement this!")