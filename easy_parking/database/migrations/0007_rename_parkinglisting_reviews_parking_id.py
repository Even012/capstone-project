# Generated by Django 5.0.3 on 2024-03-10 15:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0006_reviews"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reviews",
            old_name="ParkingListing",
            new_name="parking_id",
        ),
    ]
