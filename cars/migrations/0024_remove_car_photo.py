# Generated by Django 3.2 on 2021-06-18 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0023_auto_20210618_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='Photo',
        ),
    ]
