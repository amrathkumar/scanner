from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    code = models.CharField(max_length=100, unique=True, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class WeatherSettings(models.Model):
    city = models.CharField(max_length=100, default="Mysuru")

    def __str__(self):
        return self.city