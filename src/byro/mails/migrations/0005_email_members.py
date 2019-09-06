# Generated by Django 2.1.1 on 2018-09-11 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0009_auto_20180512_1810"),
        ("mails", "0004_email_template"),
    ]

    operations = [
        migrations.AddField(
            model_name="email",
            name="members",
            field=models.ManyToManyField(
                null=True, related_name="emails", to="members.Member"
            ),
        )
    ]
