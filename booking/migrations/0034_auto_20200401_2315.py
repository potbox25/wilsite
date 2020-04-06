# Generated by Django 3.0.3 on 2020-04-01 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0033_auto_20200401_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='payment_method',
            field=models.CharField(choices=[('Coins', 'Coins'), ('Points', 'Points'), ('Coins and Points', 'Coins and Points'), ('None', 'None')], default='Coins', max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='book_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 1, 23, 15, 20, 512568)),
        ),
        migrations.AlterField(
            model_name='review',
            name='submit_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 1, 23, 15, 20, 512568)),
        ),
    ]
