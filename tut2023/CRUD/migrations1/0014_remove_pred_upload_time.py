# Generated by Django 4.1.7 on 2023-04-23 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("CRUD", "0013_alter_pred_upload_time"),
    ]

    operations = [
        migrations.RemoveField(model_name="pred", name="upload_time",),
    ]