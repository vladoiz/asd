# Generated by Django 3.2 on 2021-05-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_category_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Icon',
            field=models.ImageField(upload_to='media', verbose_name='Путь до иконки'),
        ),
    ]