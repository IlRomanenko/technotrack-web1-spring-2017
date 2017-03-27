# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 17:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20170312_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]