# Generated by Django 3.0.3 on 2020-04-01 11:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0030_auto_20200401_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='book_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 1, 19, 14, 52, 166169)),
        ),
        migrations.AlterField(
            model_name='review',
            name='submit_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 1, 19, 14, 52, 166169)),
        ),
    ]
