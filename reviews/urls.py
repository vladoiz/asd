from django.urls import path
from . import views


urlpatterns=[
    path('', views.Show_review_list.as_view(), name='reviews')
   

    ]