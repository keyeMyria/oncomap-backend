# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_auto_20160510_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='created',
            field=models.DateTimeField(auto_created=True),
        ),
    ]