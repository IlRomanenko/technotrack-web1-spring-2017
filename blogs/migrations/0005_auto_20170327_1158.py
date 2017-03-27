# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20170327_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]