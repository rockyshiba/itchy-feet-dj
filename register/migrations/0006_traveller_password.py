# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20160618_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='traveller',
            name='password',
            field=models.CharField(default='password', max_length=50),
            preserve_default=False,
        ),
    ]
