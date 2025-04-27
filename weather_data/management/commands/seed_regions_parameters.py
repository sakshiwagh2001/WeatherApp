
# C:\Users\saksh\Desktop\Weather App\weather_project\weather_data\management\commands\seed_regions_parameters.py
# C:\Users\saksh\Desktop\Weather App\weather_project\weather_data\management\commands\seed_regions_parameters.py 

from django.core.management.base import BaseCommand
from weather_data.models import Region, Parameter

class Command(BaseCommand):
    help = 'Seed Regions and Parameters into database'

    def handle(self, *args, **kwargs):
        regions = ['UK', 'England', 'Scotland', 'Wales']
        parameters = ['Tmax', 'Tmin', 'Tmean', 'Sunshine', 'Rainfall']

        for region_name in regions:
            Region.objects.get_or_create(name=region_name)
            self.stdout.write(self.style.SUCCESS(f"Region added: {region_name}"))

        for parameter_name in parameters:
            Parameter.objects.get_or_create(name=parameter_name)
            self.stdout.write(self.style.SUCCESS(f"Parameter added: {parameter_name}"))
