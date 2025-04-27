
# C:\Users\saksh\Desktop\Weather App\weather_project\weather_data\management\commands\seed_regions_parameters.py

from django.core.management.base import BaseCommand
from weather_data.models import WeatherRecord, Region, Parameter
from weather_data.services.api_factory import get_weather_service

class Command(BaseCommand):
    help = 'Fetch and save weather data from Weather APIs'

    def handle(self, *args, **kwargs):
        weather_service = get_weather_service('met_office')  

        regions = Region.objects.all()
        parameters = Parameter.objects.all()

        for region in regions:
            for parameter in parameters:
                self.stdout.write(self.style.WARNING(f"Fetching {parameter.name} for {region.name}"))
                try:
                    raw_data = weather_service.fetch_weather_data(region.name, parameter.name)
                    self.parse_and_save_data(region, parameter, raw_data)
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error: {e}"))


                    # ✅ Save to FetchLog
                    FetchLog.objects.create(
                        region=region.name,
                        parameter=parameter.name,
                        error_message=str(e)
                    )


    def parse_and_save_data(self, region, parameter, data):
        lines = data.splitlines()[5:]

        for line in lines:
            if not line.strip():
                continue

            parts = line.split()

            if len(parts) < 13 or not parts[0].isdigit():
                continue

            year = int(parts[0])
            jan = self.safe_float(parts[1])
            feb = self.safe_float(parts[2])
            mar = self.safe_float(parts[3])
            apr = self.safe_float(parts[4])
            may = self.safe_float(parts[5])
            jun = self.safe_float(parts[6])
            jul = self.safe_float(parts[7])
            aug = self.safe_float(parts[8])
            sep = self.safe_float(parts[9])
            oct_ = self.safe_float(parts[10])
            nov = self.safe_float(parts[11])
            dec = self.safe_float(parts[12])
            annual = self.safe_float(parts[13]) if len(parts) > 13 else None

            self.stdout.write(self.style.SUCCESS(
                f"Inserting: Year={year}, Region={region.name}, Parameter={parameter.name}, "
                f"Jan={jan}, Feb={feb}, Mar={mar}, Apr={apr}, May={may}, Jun={jun}, Jul={jul}, Aug={aug}, "
                f"Sep={sep}, Oct={oct_}, Nov={nov}, Dec={dec}, Annual={annual}"
            ))

      
            WeatherRecord.objects.create(
                region=region,
                parameter=parameter,
                year=year,
                jan=jan,
                feb=feb,
                mar=mar,
                apr=apr,
                may=may,
                jun=jun,
                jul=jul,
                aug=aug,
                sep=sep,
                oct=oct_,
                nov=nov,
                dec=dec,
                annual=annual
            )

    def safe_float(self, value):
        try:
            return float(value)
        except ValueError:
            return None
 


