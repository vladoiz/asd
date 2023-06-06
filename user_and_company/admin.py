from django.contrib import admin
from .models import Person
from .models import Company


# Register your models here.
admin.site.register(Person)
admin.site.register(Company)

