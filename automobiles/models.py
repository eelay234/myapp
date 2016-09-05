from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=20)
    manufacturer = models.ForeignKey(Manufacturer)

    def __unicode__(self):
        return self.name
