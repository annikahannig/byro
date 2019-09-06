# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-03 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("bookkeeping", "0010_auto_20180113_1500")]

    operations = [
        migrations.AlterField(
            model_name="realtransaction",
            name="importer",
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="realtransaction",
            name="originator",
            field=models.CharField(max_length=500),
        ),
    ]
