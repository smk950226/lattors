# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-16 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lattors', '0010_auto_20171016_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actphoto',
            name='photo',
            field=models.ImageField(upload_to='actphoto', verbose_name='활동 사진'),
        ),
    ]
