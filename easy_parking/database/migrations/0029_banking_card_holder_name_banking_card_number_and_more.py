# Generated by Django 5.0.3 on 2024-03-21 04:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0028_parkinglisting_host_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="banking",
            name="card_holder_name",
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="banking",
            name="card_number",
            field=models.CharField(default="", max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="banking",
            name="cvv",
            field=models.CharField(default=None, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="banking",
            name="expiration_date",
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
