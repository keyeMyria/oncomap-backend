# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 02:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('imported', models.BooleanField(default=False)),
                ('imported_from', models.CharField(blank=True, max_length=255, null=True)),
                ('import_reference', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('good', 'Good'), ('bad', 'Not good'), ('neutral', 'Neutral')], max_length=255)),
                ('created', models.DateTimeField()),
                ('comment', models.CharField(max_length=555)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.Resource')),
            ],
        ),
    ]
