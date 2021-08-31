from django.urls import path

from . import views

# Todo: payment(bonus)

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/',views.create, name = 'create'),
    path('one_time_pickup/',views.one_time_pickup, name = 'one_time_pickup'),
    path('update_pickup/', views.update_pickup, name = 'update_pickup'),
    path('one_time_pickup/', views.one_time_pickup, name = 'one_time_pickup'),
    path('suspend_pickup/', views.suspend_pickup, name = 'suspend_pickup'),
    path('account_balance/', views.account_balance, name= 'account_balance')
]
