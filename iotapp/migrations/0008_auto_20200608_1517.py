# Generated by Django 3.0.7 on 2020-06-08 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iotapp', '0007_humidityreading_temperaturereading'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='device',
            new_name='devices',
        ),
    ]