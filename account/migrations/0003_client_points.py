# Generated by Django 3.0.3 on 2020-03-26 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_client_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
