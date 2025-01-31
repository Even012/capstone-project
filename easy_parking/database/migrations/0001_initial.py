# Generated by Django 5.0.3 on 2024-03-05 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=10)),
                ('user_type', models.CharField(max_length=5)),
            ],
        ),
    ]
