from django.urls import path
from . import views

urlpatterns=[
    path('clients', views.Show_clients_list.as_view(), name='admin_clients'),
    path('clients/client_<int:pk>', views.Show_client.as_view(), name='admin_client'),
    path('clients/add_client', views.Add_client.as_view(), name='admin_add_client'),
    path('clients/client_<int:pk>/update', views.Update_client.as_view(), name='admin_update_client'),
    path('clients/client_<int:pk>/delete', views.Delete_user.as_view(), name='admin_delete_client'),
    path('clients/client_<int:pk>/orders', views.Show_client_orders.as_view(), name='admin_client_orders'),


    path('admins', views.Show_admins_list.as_view(), name='admin_admins'),
    path('admins/admin_<int:pk>', views.Show_admin.as_view(), name='admin_admin'),
    path('admins/add_admin', views.Add_admin.as_view(), name='admin_add_admin'),
    path('admins/admin_<int:pk>/update', views.Update_admin.as_view(), name='admin_update_admin'),
    path('admins/admin_<int:pk>/delete', views.Delete_user.as_view(), name='admin_delete_admin'),

    path('companies', views.Show_companies_list.as_view(), name='admin_companies'),
    path('companies/company_<int:pk>', views.Show_company.as_view(), name='admin_company'),
    path('companies/add_company', views.Add_company.as_view(), name='admin_add_company'),
    path('companies/company_<int:pk>/update', views.Update_company.as_view(), name='admin_update_company'),
    path('companies/company_<int:pk>/delete', views.Delete_company.as_view(), name='admin_delete_company'),

    path('companies/company_<int:pk>/cars', views.Show_company_cars.as_view(), name='admin_company_cars'),
    path('companies/company_<int:pk>/orders', views.Show_company_orders.as_view(), name='admin_company_orders'),
    path('companies/company_<int:pk>/workers', views.Show_workers_list.as_view(), name='admin_workers'),
    path('companies/company_<int:pk>/workers/worker_<int:worker_id>', views.Show_worker.as_view(), name='admin_worker'),
    path('companies/company_<int:pk>/workers/add_worker', views.Add_worker.as_view(), name='admin_add_worker'),
    path('companies/company_<int:pk>/workers/worker_<int:worker_id>/update', views.Update_worker.as_view(), name='admin_update_worker'),
    path('companies/company_<int:pk>/workers/worker_<int:worker_id>/delete', views.Delete_worker.as_view(), name='admin_delete_worker')

    ]
