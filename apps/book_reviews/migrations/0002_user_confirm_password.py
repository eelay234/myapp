# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirm_password',
            field=models.CharField(default='', max_length=45),
            preserve_default=False,
        ),
    ]
