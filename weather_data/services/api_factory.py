

# C:\Users\AGT25.DESKTOP-LKQKFEQ\Desktop\alpha\Django\weather_project\weather_data\services\api_factory.py

from .met_office_service import MetOfficeService

def get_weather_service(source_name):
    if source_name == 'met_office':
        return MetOfficeService()
    else:
        raise ValueError("Invalid weather source")