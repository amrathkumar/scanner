from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name

class WeatherSettings(models.Model):
    city = models.CharField(max_length=100, default="Mysuru")

    def __str__(self):
        return self.city