# Generated by Django 5.0.3 on 2024-03-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0014_reviews"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviews",
            name="user_id",
            field=models.IntegerField(),
        ),
    ]
