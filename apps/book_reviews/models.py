from __future__ import unicode_literals
from django.core.exceptions import ValidationError

from django.db import models

# Create your models here.
def validateLengthGreaterThanThree(value):
    if len(value) < 4:
         raise ValidationError(
            '{} must be longer than: {}'.format(value)
         )
class User(models.Model):
    name = models.CharField(max_length=100, validators = [validateLengthGreaterThanThree])
    alias = models.CharField(max_length=100, validators = [validateLengthGreaterThanThree])
    password = models.CharField(max_length=45)
    confirm_password = models.CharField(max_length=45)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.alias

class Book(models.Model):
    name = models.CharField(max_length=100)
    author= models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField(max_length=1000)
    writer = models.ForeignKey(User, related_name="writer")
    book = models.ForeignKey(Book, related_name="book")
    rating = models.IntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.text
