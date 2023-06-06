from datetime import date
from django.db import models

class Car(models.Model):
    transmission_list=[
        (0 ,'Механическая'),
        (1, 'Автоматическая')
    ]
    engine_list=[
        (0 ,'Бензиновый'),
        (1, 'Дизельный')
    ]
    car_type_list=[
        (0 ,'Седан'),
        (1, 'Кроссовер'),
        (2 ,'Универсал'),
        (3 ,'Хэтчбек'),
        (4 ,'Купе'),
        (5 ,'Микро')
    ]
    drive_list=[
        (0 ,'Полный'),
        (1, 'Задний'),
        (2 ,'Передний')
    ]
    wheel_drive_list=[
        (0 ,'Правый'),
        (1, 'Левый')
    ]
    CompanyID=models.ForeignKey( 'user_and_company.Company', verbose_name='ID Компании', on_delete=models.PROTECT, blank=True)
    Location=models.CharField('Расположение', max_length=250, blank=True, null=True)
    # Photo=models.ImageField(verbose_name='Фото ТС', upload_to='img_cars', blank=True, null=True, default='' )
    Photos = models.JSONField('', default="{}")
    RentCondition=models.TextField('Условия аренды', blank=True, null=True)
    Header=models.CharField('Заголовок', max_length=150, blank=True, null=True)
    Driver=models.BooleanField('Водитель', blank=True, null=True)
    Status=models.BooleanField('Статус', blank=True, null=True)
    CategoryID=models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT)
    CategoryVU=models.CharField('Категория ВУ', max_length=250, blank=True, null=True)
    DateDel=models.DateField('Дата удаления', blank=True, null=True)
    FixedRate=models.DecimalField('Фиксированная ставка', max_digits=5, decimal_places=2, blank=True, null=True )
    Percent=models.DecimalField('Комиссия', max_digits=5, decimal_places=2, blank=True, null=True )

    Brand_and_name=models.CharField('Марка и модель',max_length=150, blank=True, null=True)
    Transmission=models.IntegerField('Коробка',blank=True, null=True, choices=transmission_list, default=0)
    Engine=models.IntegerField('Двигатель', blank=True, null=True, choices=engine_list, default=0)
    Car_type=models.IntegerField('Кузов', blank=True, null=True, choices=car_type_list, default=0)
    Drive=models.IntegerField('Привод', blank=True, null=True, choices=drive_list, default=0)
    Wheel_drive=models.IntegerField('Руль', blank=True, null=True, choices=wheel_drive_list, default=0)
    Year=models.IntegerField('Год', blank=True, null=True)
    Power=models.IntegerField('Мощность', blank=True, null=True)
    Price=models.IntegerField('Стоимость', blank=True, null=True)
    
    def __str__(self):
        return self.Brand_and_name

    class Meta:
        verbose_name='Автомобиль'
        verbose_name_plural='Автомобили'


    def add_car(car, request, json):
        car.Photos = json
        car.Header = request.POST.get('Header')
        car.CategoryID_id =request.POST.get('CategoryID')
        car.CompanyID_id =request.POST.get('CompanyID')
        car.Brand_and_name = request.POST.get('Brand_and_name')
        car.Car_type = request.POST.get('Car_type')
        car.Engine = request.POST.get('Engine')
        car.Transmission = request.POST.get('Transmission')
        car.Drive = request.POST.get('Drive')
        car.Wheel_drive = request.POST.get('Wheel_drive')
        car.Year = request.POST.get('Year')
        car.Driver = request.POST.get('Driver')
        car.Power = request.POST.get('Power')
        car.CategoryVUID = request.POST.get('CategoryVUID')
        car.Price = request.POST.get('Price')
        car.FixedRate = request.POST.get('FixedRate')
        car.Percent = request.POST.get('Percent')
        car.Location = request.POST.get('Location')
        car.RentCondition = request.POST.get('RentCondition')
        car.save()
        return car

    def update_car(car, request, pk):   
        car = Car.objects.get(id=pk)
        car.Header = request.POST.get('Header')
        car.CategoryID_id =request.POST.get('CategoryID')
        car.CompanyID_id =request.POST.get('CompanyID')
        car.Brand_and_name = request.POST.get('Brand_and_name')
        car.Car_type = request.POST.get('Car_type')
        car.Engine = request.POST.get('Engine')
        car.Transmission = request.POST.get('Transmission')
        car.Drive = request.POST.get('Drive')
        car.Wheel_drive = request.POST.get('Wheel_drive')
        car.Year = request.POST.get('Year')
        car.Driver = request.POST.get('Driver')
        car.Power = request.POST.get('Power')
        car.CategoryVUID = request.POST.get('CategoryVUID')
        car.Price = request.POST.get('Price')
        car.FixedRate = request.POST.get('FixedRate')
        car.Percent = request.POST.get('Percent')
        car.Location = request.POST.get('Location')
        car.RentCondition = request.POST.get('RentCondition')
        car.save()
        return car

    def delete_car(pk):
        car = Car.objects.get(id=pk)
        car.DateDel = date.today()
        car.save()
        return True

    def hidden_car(pk):   
        car = Car.objects.get(id=pk)
        car.Status = 1
        car.save()
        return car

    def visible_car(pk):   
        car = Car.objects.get(id=pk)
        car.Status = 0
        car.save()
        return car


class Category(models.Model):
    NameCat=models.CharField('Название', max_length=100)
    Icon=models.ImageField(verbose_name='Путь до иконки', upload_to='img_category')
    DateDel=models.DateField('Дата удаления')
    Percent=models.DecimalField('Комиссия', max_digits=5, decimal_places=2 )
    FixedRate=models.DecimalField('Фиксированная ставка', max_digits=5, decimal_places=2 )

    def __str__(self):
        return self.NameCat

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'









# Create your models here.
