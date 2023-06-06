from django.db import models
from django.db.models.fields import DateField
from user_and_company.models import Person
# from orders.models import Contract
from datetime import date
from django.contrib import messages
import datetime


# Create your models here.
class FeedBackAndComment(models.Model):
    User=models.ForeignKey('user_and_company.Person', verbose_name='Админ или сотрудник', on_delete=models.PROTECT, blank=True, null=True)
    Contract=models.ForeignKey('orders.Contract', verbose_name='Заказ', on_delete=models.PROTECT, blank=True, null=True)
    Name=models.CharField('Имя', max_length=50, default='')
    Message = models.TextField('Сообщение', blank=True, null=True)
    Status=models.BooleanField('Статус сообщения обратной связи', blank=True, null=True)
    Type=models.BooleanField('Тип сообщения', blank=True, null=True)
    PhoneEmail=models.CharField('Телефон или почта', max_length=12, default='')
    DateDel=models.DateField('Дата удаления', blank=True, null=True)
    Date=models.DateField('Дата', blank=True, null=True)

    def __str__(self):
        return self.Type + self.Message

    class Meta:
        verbose_name='Комментарий или сообщение'
        verbose_name_plural='Комментарии или сообщения'
        ordering = ['-id']

    def add_feedback(feedback, request):
        feedback.Name = request.POST.get('Name')
        feedback.PhoneEmail = request.POST.get('PhoneEmail')
        feedback.Message = request.POST.get('Message')
        feedback.Status = 0
        feedback.Type = 0
        feedback.Date = date.today()
        feedback.save()
        # messages.success(request, 'Ваше сообщение успешно отправлено!!')
        return feedback

    def update_feedback(feedback, request, pk):
        feedback = FeedBackAndComment.objects.get(id=pk)
        print(request.POST.get('Status'))
        if (request.POST.get('Status')== 'on'):
            status = 1
        else:
            status = 0
        feedback.Status = status
        feedback.save()
        return feedback

    def delete_feedback(pk):
        feedback = FeedBackAndComment.objects.get(id=pk)
        feedback.DateDel = date.today()
        feedback.save()
        return True
        
    def add_comment(id ,comment):
        person_from = 7
        comment = FeedBackAndComment.objects.create(Contract_id=id,Date = datetime.datetime.now(), Message = comment , User_id = person_from, Status = 0, Type = 1)
        comment.save()
        return comment

    def delete_comment(comment):
        k = FeedBackAndComment.objects.filter(id = comment)
        k.delete()
        return True
