# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveller',
            name='image',
            field=models.ImageField(blank=True, default='static/images/feet.png', max_length=10000, null=True, upload_to=None),
        ),
    ]
