# Generated by Django 4.2.6 on 2023-10-29 20:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ApiDrinkSaver", "0004_apikey"),
    ]

    operations = [
        migrations.AddField(
            model_name="apikey",
            name="name",
            field=models.CharField(default="", max_length=255),
        ),
    ]
