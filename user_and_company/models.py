from django.db import models
from datetime import date
# Create your models here.
class Person(models.Model):

    position_list=[
        (0 ,'Администратор'),
        (1, 'Сотрудник'),
        (2, 'Клиент')
    ]

    Company=models.ForeignKey('Company', verbose_name='Компания', on_delete=models.PROTECT, blank=True, null=True)
    Name=models.CharField('Имя', max_length=50)
    Fname=models.CharField('Фамилия', max_length=50)
    Date=models.DateField('Дата рождения', blank=True, null=True)
    Phone=models.CharField('Телефон', max_length=12)
    Email=models.EmailField('Email')
    Passport=models.CharField('Паспорт', max_length=50, blank=True, null=True)
    Position=models.IntegerField('Позиция', blank=True, null=True, choices=position_list, default=0)   
    Comment=models.TextField('Комментарий', blank=True, null=True)
    NumVU=models.CharField('Номер ВУ', max_length=50, blank=True, null=True)
    Password=models.CharField('Пароль', max_length=150, blank=True, null=True)
    DateDel=models.DateField('Дата удаления', blank=True, null=True)
    CategoryVU = models.JSONField('Категории', blank=True, null=True, default="{}")
    # img = models.ImageField(upload_to='test', blank=True, null=True,)
    # images = models.JSONField('Картинки', blank=True, null=True, default="{}")
    
    
    def __str__(self):
        return self.Name + self.Fname + self.Phone

    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'

    def add_client(client, request, data):
        client.Name = request.POST.get('Name')
        client.Fname = request.POST.get('Fname')
        client.Email = request.POST.get('Email')
        client.Phone = request.POST.get('Phone')
        client.Date = request.POST.get('Date')
        client.Passport = request.POST.get('Passport')
        client.NumVU = request.POST.get('NumVU')
        client.Position = 2
        client.CategoryVU = data
        client.save()
        return client

    def update_client(client, request, pk, data):
        client = Person.objects.get(id=pk)
        client.Name = request.POST.get('Name')
        client.Fname = request.POST.get('Fname')
        client.Email = request.POST.get('Email')
        client.Phone = request.POST.get('Phone')
        client.Date = request.POST.get('Date')
        client.Passport = request.POST.get('Passport')
        client.NumVU = request.POST.get('NumVU')
        client.CategoryVU = data
        client.save()
        return client

    def delete_user(pk):
        user = Person.objects.get(id=pk)
        user.DateDel = date.today()
        user.save()
        return True
#########################################################################
    def add_admin(admin, request):
        admin.Name = request.POST.get('Name')
        admin.Fname = request.POST.get('Fname')
        admin.Email = request.POST.get('Email')
        admin.Phone = request.POST.get('Phone')
        admin.Comment = request.POST.get('Comment')
        admin.Position = 0
        admin.save()
        return admin

    def update_admin(admin, request, pk):
        admin = Person.objects.get(id=pk)
        admin.Name = request.POST.get('Name')
        admin.Fname = request.POST.get('Fname')
        admin.Email = request.POST.get('Email')
        admin.Phone = request.POST.get('Phone')
        admin.Comment = request.POST.get('Comment')
        admin.save()
        return admin

    def add_worker(worker, request, pk):
        worker.Name = request.POST.get('Name')
        worker.Fname = request.POST.get('Fname')
        worker.Email = request.POST.get('Email')
        worker.Phone = request.POST.get('Phone')
        worker.Comment = request.POST.get('Comment')
        worker.Company_id = pk
        worker.Position = 1
        worker.save()
        return worker

    def update_worker(worker, request, pk):
        worker = Person.objects.get(id=pk)
        worker.Name = request.POST.get('Name')
        worker.Fname = request.POST.get('Fname')
        worker.Email = request.POST.get('Email')
        worker.Phone = request.POST.get('Phone')
        worker.Comment = request.POST.get('Comment')
        worker.save()
        return worker
#######################################################################

class Company(models.Model):
    Name=models.CharField('Название', max_length=50)
    Phone=models.CharField('Телефон', max_length=12)
    Email=models.EmailField('Email')
    Note=models.TextField('Примечание', blank=True, null=True)
    DateDel=models.DateField('Дата удаления', blank=True, null=True)
    ContactFIO=models.CharField('Контактное лицо',  max_length=150, blank=True)
    ContactPhone=models.CharField('Телефон',  max_length=12)
    ContactEmail=models.EmailField('Email')

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name='Компания'
        verbose_name_plural='Компании'
###################################################################
    def add_company(company, request):
        company.Name = request.POST.get('Name')
        company.Email = request.POST.get('Email')
        company.Phone = request.POST.get('Phone')
        company.Note = request.POST.get('Note')
        company.ContactFIO = request.POST.get('ContactFIO')
        company.ContactEmail = request.POST.get('ContactEmail')
        company.ContactPhone = request.POST.get('ContactPhone')
        company.save()
        return company

    def update_company(company, request, pk):   
        company = Company.objects.get(id=pk)
        company.Name = request.POST.get('Name')
        company.Email = request.POST.get('Email')
        company.Phone = request.POST.get('Phone')
        company.Note = request.POST.get('Note')
        company.ContactFIO = request.POST.get('ContactFIO')
        company.ContactEmail = request.POST.get('ContactEmail')
        company.ContactPhone = request.POST.get('ContactPhone')
        company.save()
        return company

    def delete_company(pk):
        company = Company.objects.get(id=pk)
        company.DateDel = date.today()
        company.save()
        return True
######################################################################
    