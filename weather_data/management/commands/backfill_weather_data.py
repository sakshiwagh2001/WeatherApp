# weather_data/management/commands/backfill_weather_data.py

from django.core.management.base import BaseCommand
from weather_data.models import Region, Parameter
from weather_data.services.api_factory import get_weather_service

class Command(BaseCommand):
    help = 'Backfill historical weather data'

    def handle(self, *args, **kwargs):
        weather_service = get_weather_service('met_office')

        regions = Region.objects.all()
        parameters = Parameter.objects.all()

        for region in regions:
            for parameter in parameters:
                self.stdout.write(self.style.WARNING(f"Backfilling {parameter.name} for {region.name}"))
                try:
                    raw_data = weather_service.fetch_weather_data(region.name, parameter.name, backfill=True)
                    # ✅ Reuse existing parse/save logic or create separate method
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Backfill error: {e}"))
