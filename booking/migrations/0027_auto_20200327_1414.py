# Generated by Django 3.0.3 on 2020-03-27 06:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0026_auto_20200327_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='computer_fee',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='book_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 14, 14, 36, 526626)),
        ),
        migrations.AlterField(
            model_name='review',
            name='submit_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 14, 14, 36, 526626)),
        ),
    ]