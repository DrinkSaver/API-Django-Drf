# Generated by Django 4.2.6 on 2023-10-30 12:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("socialaccount", "0005_socialtoken_nullable_app"),
        ("ApiDrinkSaver", "0008_alter_customemailaddress_custom_user"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CustomUser",
            new_name="User",
        ),
    ]