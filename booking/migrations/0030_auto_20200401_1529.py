# Generated by Django 3.0.3 on 2020-04-01 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0029_auto_20200401_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booker',
            field=models.CharField(default='none', max_length=30),
        ),
        migrations.AlterField(
            model_name='booking',
            name='book_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 1, 15, 29, 1, 519103)),
        ),
        migrations.AlterField(
            model_name='review',
            name='submit_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 1, 15, 29, 1, 520103)),
        ),
    ]
