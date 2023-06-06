# Generated by Django 3.2 on 2021-05-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameCat', models.CharField(max_length=100, verbose_name='Название')),
                ('Icon', models.TextField(verbose_name='Путь до иконки')),
                ('DateDel', models.DateField(verbose_name='Дата удаления')),
                ('Percent', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Комиссия')),
                ('FixedRate', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Фиксированная ставка')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]