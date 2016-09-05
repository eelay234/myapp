# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-04 07:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]