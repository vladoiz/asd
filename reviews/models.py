from django.db import models

# Create your models here.

class Reviews(models.Model):
    ClientID=models.ForeignKey('user_and_company.Person', verbose_name='ID клиента',  on_delete=models.PROTECT, blank=True, null=True)
    Review=models.TextField('Текст отзыва')
    Photo=models.CharField('Фото', max_length=250)
    Status=models.BooleanField('Статус')
    Date=models.DateField('Дата отзыва')
    DateDel=models.DateField('Дата удаления')


    def __str__(self):
        return self.Review

    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural='Отзывы'


