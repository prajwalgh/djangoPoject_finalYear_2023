# Generated by Django 4.1.7 on 2023-04-23 08:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("CRUD", "0011_pred"),
    ]

    operations = [
        migrations.AddField(
            model_name="pred",
            name="upload_time",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]