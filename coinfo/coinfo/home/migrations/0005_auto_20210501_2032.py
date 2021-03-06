# Generated by Django 3.2 on 2021-05-01 15:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210501_1952'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Home_Icu',
        ),
        migrations.AddField(
            model_name='hospital',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 1, 20, 32, 32, 260281)),
        ),
        migrations.AddField(
            model_name='medicine',
            name='time_stamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 1, 20, 32, 32, 261278)),
        ),
        migrations.AddField(
            model_name='oxygen',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 1, 20, 32, 32, 260281)),
        ),
        migrations.AddField(
            model_name='plasma',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 1, 20, 32, 32, 261278)),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='price',
            field=models.CharField(blank=True, default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='oxygen',
            name='price',
            field=models.CharField(blank=True, default='', max_length=7),
        ),
    ]
