# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20171008_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='filtered_image',
            field=models.ImageField(upload_to='uploads/%Y/%m/%d/filtered'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='uploads/%Y/%m/%d/orig'),
        ),
    ]
