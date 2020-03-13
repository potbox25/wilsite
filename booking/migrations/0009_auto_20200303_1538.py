# Generated by Django 3.0.3 on 2020-03-03 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_auto_20200303_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='venue',
            field=models.CharField(choices=[('Conference Room A', 'Conference Room A'), ('Conference Room B', 'Conference Room B'), ('Joined Conference Room', 'Joined Conference Room'), ('Coworking Space', 'Coworking Space')], default='Coworking Space', max_length=30),
        ),
    ]