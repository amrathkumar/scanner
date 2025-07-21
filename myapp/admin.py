from django.contrib import admin
from .models import Item
from .models import WeatherSettings

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')  

admin.site.register(WeatherSettings)