# Generated by Django 5.0.3 on 2024-03-24 03:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0036_rename_cardetails_carddetails"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CarDetials",
            new_name="CarDetails",
        ),
    ]
