# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-21 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20171018_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='sub_major',
            field=models.CharField(blank=True, help_text='해당하는 경우에만 작성해 주세요.', max_length=30, verbose_name='복수/부전공'),
        ),
    ]
