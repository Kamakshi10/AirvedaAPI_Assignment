# Generated by Django 3.0.7 on 2020-06-07 15:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('iotapp', '0003_auto_20200607_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemperatureReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iotapp.device')),
            ],
        ),
        migrations.CreateModel(
            name='HumidityReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Humidity', models.FloatField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iotapp.device')),
            ],
        ),
    ]
