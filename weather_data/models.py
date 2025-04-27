

# C:\Users\saksh\Desktop\Weather App\weather_project\weather_data\models.py

from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Parameter(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class WeatherRecord(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    year = models.IntegerField()
    jan = models.FloatField(null=True)
    feb = models.FloatField(null=True)
    mar = models.FloatField(null=True)
    apr = models.FloatField(null=True)
    may = models.FloatField(null=True)
    jun = models.FloatField(null=True)
    jul = models.FloatField(null=True)
    aug = models.FloatField(null=True)
    sep = models.FloatField(null=True)
    oct = models.FloatField(null=True)
    nov = models.FloatField(null=True)
    dec = models.FloatField(null=True)
    annual = models.FloatField(null=True)

    def __str__(self):
        return f"{self.region.name} - {self.parameter.name} - {self.year}"



class FetchLog(models.Model):
    region = models.CharField(max_length=100)
    parameter = models.CharField(max_length=100)
    error_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Fetch Error for {self.region} - {self.parameter}"