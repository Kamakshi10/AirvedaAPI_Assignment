# Generated by Django 3.0.7 on 2020-06-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iotapp', '0004_humidityreading_temperaturereading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humidityreading',
            name='Humidity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='temperaturereading',
            name='temperature',
            field=models.IntegerField(),
        ),
    ]
