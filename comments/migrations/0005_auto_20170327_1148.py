# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_comment_creation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='creation_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]