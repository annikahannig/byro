# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("members", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="member",
            name="address",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name="member",
            name="name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="member",
            name="number",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="member",
            name="email",
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]
