# Generated by Django 2.0 on 2017-12-06 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("profile", "0003_auto_20171012_2032")]

    operations = [
        migrations.AlterField(
            model_name="memberprofile",
            name="birth_date",
            field=models.DateField(null=True, verbose_name="Birth date"),
        ),
        migrations.AlterField(
            model_name="memberprofile",
            name="nick",
            field=models.CharField(max_length=200, null=True, verbose_name="Nick"),
        ),
        migrations.AlterField(
            model_name="memberprofile",
            name="phone_number",
            field=models.CharField(
                blank=True, max_length=32, null=True, verbose_name="Phone number"
            ),
        ),
    ]
