# Generated by Django 3.0.3 on 2020-03-04 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_auto_20200303_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='computers',
            field=models.IntegerField(default=0),
        ),
    ]
