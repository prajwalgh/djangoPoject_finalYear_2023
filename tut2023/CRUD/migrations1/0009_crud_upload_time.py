# Generated by Django 4.1.7 on 2023-04-21 19:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CRUD", "0008_remove_crud_upload_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="crud",
            name="upload_time",
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 1, 0, 0)),
        ),
    ]
