# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-14 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lattors', '0005_auto_20170918_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='actphoto', verbose_name='활동 사진')),
                ('year', models.PositiveIntegerField(choices=[('2017', '2017년'), ('2016', '2016년'), ('2015', '2015년'), ('2014', '2014년'), ('2013', '2013년 이전')], default=2017, verbose_name='활동 년도')),
                ('date', models.CharField(help_text='0000.00.00과 같이 입력해 주세요.', max_length=20, verbose_name='활동 날짜')),
                ('site', models.CharField(max_length=100, verbose_name='활동 장소')),
            ],
        ),
    ]