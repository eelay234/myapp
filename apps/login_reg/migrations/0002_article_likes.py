# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
