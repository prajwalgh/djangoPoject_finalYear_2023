# Generated by Django 4.1.7 on 2023-04-21 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CRUD", "0006_crud_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="crud",
            name="upload_time",
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
    ]
