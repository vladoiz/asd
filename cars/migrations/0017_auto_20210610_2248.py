# Generated by Django 3.2 on 2021-06-10 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0016_auto_20210610_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_type',
            new_name='Car_type',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='drive',
            new_name='Drive',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='engine',
            new_name='Engine',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='power',
            new_name='Power',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='price',
            new_name='Price',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='transmission',
            new_name='Transmission',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='wheel_drive',
            new_name='Wheel_drive',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='year',
            new_name='Year',
        ),
    ]