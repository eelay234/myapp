"""Admin for Automobiles"""
from django.contrib import admin

from automobiles.models import Manufacturer, Car
# Register your models here.
admin.site.register(Car)
admin.site.register(Manufacturer)
