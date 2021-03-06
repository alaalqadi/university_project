# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-05-04 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='')),
                ('status', models.CharField(blank=True, choices=[('open', 'open'), ('deleted', 'deleted')], max_length=200, null=True)),
            ],
        ),
    ]
