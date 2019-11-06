from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Substation

@admin.register(Substation)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')