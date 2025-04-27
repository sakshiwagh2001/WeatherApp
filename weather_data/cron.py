# weather_data/cron.py

from django_cron import CronJobBase, Schedule
from django.core.management import call_command

class FetchWeatherCronJob(CronJobBase):
    RUN_EVERY_MINS = 1440  # 24 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'weather_data.fetch_weather_cron'  

    def do(self):
        call_command('fetch_weather_data')
