# Generated by Django 3.0.7 on 2020-06-07 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iotapp', '0002_auto_20200607_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
