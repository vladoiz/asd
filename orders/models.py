import datetime
from django.db import models
from datetime import date, timedelta
import decimal
from django.db.models.fields import DecimalField
from cars.models import Car
from feedback_and_comments.models import FeedBackAndComment
from user_and_company.models import Person



# Create your models here.

class Contract(models.Model):
    Client=models.ForeignKey('user_and_company.Person', verbose_name='Клиент', on_delete=models.PROTECT, blank=True, null=True)
    Car=models.ForeignKey('cars.Car', verbose_name='Авто', on_delete=models.PROTECT, blank=True, null=True, related_name='car')
    DateStartContract=models.DateField('Дата начала', blank=True, null=True)
    DateEndContract=models.DateField('Дата окончания', blank=True, null=True)
    Driver=models.BooleanField('Нужен ли водитель', blank=True, null=True)
    Note=models.TextField('Примечание', blank=True, null=True)
    Status=models.IntegerField('Статус заказа', blank=True, null=True)
    Comission=models.DecimalField('Комиссия', max_digits=10, decimal_places=2, blank=True, null=True )
    Cost=models.IntegerField('Стоимость', blank=True, null=True )
    DateDel=models.DateField('Дата удаления', blank=True, null=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name='Заказ'
        verbose_name_plural='Заказы'
        ordering = ['-id']

    def add_order(order, request):
        car = Car.objects.get(id=int(request.POST.get('Car')))
        end = datetime.datetime.strptime(request.POST.get('DateEndContract'), '%Y-%m-%d')
        start = datetime.datetime.strptime(request.POST.get('DateStartContract'), '%Y-%m-%d')
        if (end == start):
            rez = 1
        else:
            rez = (end-start).days
        cost =  rez * car.Price
        order.Client_id = request.POST.get('Client')
        order.Car_id = request.POST.get('Car')
        order.DateStartContract = request.POST.get('DateStartContract')
        order.DateEndContract = request.POST.get('DateEndContract')
        order.Driver = request.POST.get('Driver')
        order.Note = request.POST.get('Note')
        order.Status = 0
        if (int(request.POST.get('Driver')) == 1):
            driver = 1500
        else: 
            driver = 0
        order.Cost = cost + driver
        car_per = car.Percent
        car_fix = car.FixedRate + decimal.Decimal(driver)
        per1 = car_per * decimal.Decimal(0.01)
        per2 = round((per1 * decimal.Decimal(cost)) + car_fix , 2)
        order.Comission = per2
        order.save()
        return order

    def add_order_client(order, request, pk):
        car = Car.objects.get(id=pk)
        end = datetime.datetime.strptime(request.POST.get('DateEndContract'), '%Y-%m-%d')
        start = datetime.datetime.strptime(request.POST.get('DateStartContract'), '%Y-%m-%d')
        if (end == start):
            rez = 1
        else:
            rez = (end-start).days
        if (request.POST.get("Driver") == 'on'):
            order.Driver = True
            driver = 1500
        else:
            order.Driver = False
            driver = 0
        order.Client_id = 10
        order.Car_id = car.id
        order.DateStartContract = request.POST.get('DateStartContract')
        order.DateEndContract = request.POST.get('DateEndContract')
        cost =  rez * car.Price
        order.Cost = cost + driver
        car_per = car.Percent
        car_fix = car.FixedRate + decimal.Decimal(driver)
        per1 = car_per * decimal.Decimal(0.01)
        per2 = round((per1 * decimal.Decimal(cost)) + car_fix , 2)
        order.Comission = per2
        order.Status = 0
        order.save()
        return order

    def update_order(order, request, pk):
        order = Contract.objects.get(id=pk)
        car = Car.objects.get(id=int(request.POST.get('Car')))
        end = datetime.datetime.strptime(request.POST.get('DateEndContract'), '%Y-%m-%d')
        start = datetime.datetime.strptime(request.POST.get('DateStartContract'), '%Y-%m-%d')
        rez = (end-start).days
        if  ((request.POST.get('AmmountPaid')) =='' or int(request.POST.get('AmmountPaid')) != 0 ):
            sumpay= Payment.add_pay(pk, request.POST.get('AmmountPaid'))
        order.Car_id = request.POST.get('Car')
        order.DateStartContract = request.POST.get('DateStartContract')
        order.DateEndContract = request.POST.get('DateEndContract')
        order.Driver = request.POST.get('Driver')
        order.Note = request.POST.get('Note')
        
        if (request.POST.get("Driver") == "1"):
            order.Driver = True
            driver = 1500
        else:
            order.Driver = False
            driver = 0
        cost =  rez * car.Price
        order.Cost = cost + driver
        car_per = car.Percent
        car_fix = car.FixedRate + decimal.Decimal(driver)
        per1 = car_per * decimal.Decimal(0.01)
        per2 = round((per1 * decimal.Decimal(cost)) + car_fix , 2)
        order.Comission = per2
        order.save()
        return order

    # def delete_comment(pk):
    #     comment = FeedBackAndComment.objects.get(id=pk)
    #     comment.DateDel = date.today()
    #     comment.save()
    #     return True
    def end_order(pk):
        order = Contract.objects.get(id=pk)
        order.Status = 2
        order.save()
        return order

    def cancel_order(pk):
        order = Contract.objects.get(id=pk)
        order.Status = 1
        order.save()
        return order

class Payment(models.Model):
    Contract = models.ForeignKey('Contract', verbose_name='Заказ', on_delete=models.PROTECT, blank=True, null=True)
    DateOfPayment=models.DateField('Дата оплаты', blank=True, null=True)
    AmmountPaid=models.IntegerField('Сумма платежа', blank=True, null=True )

    def __str__(self):
        return self.AmmountPaid

    class Meta:
        verbose_name='Платеж'
        verbose_name_plural='Платежи'
    
    def add_pay(id, sum):
        pay = Payment.objects.create(Contract_id=id,DateOfPayment = date.today(), AmmountPaid = sum)
        pay.save()
        return pay

class Message(models.Model):
    Contract = models.ForeignKey('Contract', verbose_name='Заказ', on_delete=models.PROTECT, blank=True, null=True)
    From = models.ForeignKey('user_and_company.Person', verbose_name='Отправитель', on_delete=models.PROTECT, blank=True, null=True)
    Message = models.TextField('Сообщение', blank=True, null=True)
    Date=models.DateTimeField('Дата', blank=True, null=True)
    Status=models.BooleanField('Статус', blank=True, null=True)

    def __str__(self):
        return self.Contract

    class Meta:
        verbose_name='Сообщение'
        verbose_name_plural='Сообщения'
    
    def add_message(id, message):
        person_from = 2
        mes = Message.objects.create(Contract_id=id,Date = datetime.datetime.now(), Message = message , From_id = person_from)
        mes.save()
        return mes