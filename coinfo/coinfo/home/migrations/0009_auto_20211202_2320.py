# Generated by Django 3.2.9 on 2021-12-02 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210501_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 2, 23, 20, 46, 802899)),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='time_stamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 2, 23, 20, 46, 802899)),
        ),
        migrations.AlterField(
            model_name='oxygen',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 2, 23, 20, 46, 802899)),
        ),
        migrations.AlterField(
            model_name='plasma',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 2, 23, 20, 46, 802899)),
        ),
    ]
