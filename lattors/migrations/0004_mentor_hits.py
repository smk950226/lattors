# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-10 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lattors', '0003_auto_20170828_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='hits',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
