from django.contrib import admin
from restaurant.models import Pizza
from restaurant.models import Topping

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Topping)
