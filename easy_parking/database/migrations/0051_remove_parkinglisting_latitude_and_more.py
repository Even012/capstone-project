# Generated by Django 5.0.3 on 2024-04-01 12:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0050_alter_parkinglisting_latitude_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="parkinglisting",
            name="latitude",
        ),
        migrations.RemoveField(
            model_name="parkinglisting",
            name="longitude",
        ),
    ]
