# Generated by Django 3.2 on 2021-06-12 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_contract_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='Cost',
            field=models.IntegerField(blank=True, null=True, verbose_name='Стоимость'),
        ),
    ]