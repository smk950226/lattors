# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-19 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lattors', '0012_talkmentor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talkmentor',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='talkmentor',
            name='nickname',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
