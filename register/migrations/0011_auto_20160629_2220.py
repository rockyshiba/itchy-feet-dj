# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_auto_20160629_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveller',
            name='image',
            field=models.ImageField(blank=True, default='/static/images/feet.png', max_length=10000, null=True, upload_to=None),
        ),
    ]
