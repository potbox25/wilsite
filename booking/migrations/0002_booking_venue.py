# Generated by Django 3.0.3 on 2020-02-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='venue',
            field=models.CharField(choices=[('conf', 'Conference Room'), ('conf2', 'Joined Conference Room'), ('coworking', 'Coworking Space')], default='coworking', max_length=30),
        ),
    ]
