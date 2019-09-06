# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 11:20
from __future__ import unicode_literals

import byro.common.models.auditable
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("members", "0002_auto_20171012_1857")]

    operations = [
        migrations.CreateModel(
            name="Membership",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start", models.DateField(verbose_name="start")),
                ("end", models.DateField(blank=True, null=True, verbose_name="end")),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The amount to be paid in the chosen interval",
                        max_digits=8,
                        verbose_name="amount",
                    ),
                ),
                (
                    "interval",
                    models.IntegerField(
                        choices=[
                            (1, "monthly"),
                            (3, "quarterly"),
                            (6, "biannually"),
                            (12, "annually"),
                        ],
                        help_text="How often does the member pay their fees?",
                        verbose_name="interval",
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="memberships",
                        to="members.Member",
                    ),
                ),
            ],
            bases=(byro.common.models.auditable.Auditable, models.Model),
        ),
        migrations.CreateModel(
            name="MembershipType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="name")),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Please enter the yearly fee for this membership type.",
                        max_digits=8,
                        verbose_name="amount",
                    ),
                ),
            ],
            bases=(byro.common.models.auditable.Auditable, models.Model),
        ),
    ]
