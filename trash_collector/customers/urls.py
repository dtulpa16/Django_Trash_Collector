from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns
# TODO: customer details,suspend,set up one time pick-up, payment(bonus)

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/',views.create, name = 'create'),
    path('update_pickup/', views.update_pickup, name = 'update_pickup'),
<<<<<<< HEAD
    path('suspend_pickup/', views.suspend_pickup, name = 'suspend_pickup'),
    path('balance/', views.account_balance, name= 'accound_balance')
=======
<<<<<<< HEAD
    path('one_time_pickup/', views.one_time_pickup, name = 'one_time_pickup'),
=======
>>>>>>> ef529b13f98681e5f9bda4d1110b4edd9a904dee
    path('suspend_pickup/', views.suspend_pickup, name = 'suspend_pickup')
>>>>>>> 1d7dbb1787081f45f89a3aef60119e0f891c1c1a
]

