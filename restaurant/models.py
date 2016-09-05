from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Pizza(models.Model):
    toppings  = models.ManyToManyField(Topping)
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name
