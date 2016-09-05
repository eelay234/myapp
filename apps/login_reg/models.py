from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField(max_length=254)
    body = models.TextField()
    author = models.CharField(max_length=200,blank=True)
    pub_date = models.DateTimeField('date published', default=datetime.now,blank=True)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name="comments")
    text = models.TextField()
    author = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=datetime.now,blank=True)
    def __unicode__(self):
        return self.text
