# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-13 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_traveller_terms'),
    ]

    operations = [
        migrations.AddField(
            model_name='traveller',
            name='username',
            field=models.CharField(default='foot', max_length=50),
            preserve_default=False,
        ),
    ]