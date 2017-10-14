# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-14 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_myuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True, verbose_name='E-mail'),
            preserve_default=False,
        ),
    ]