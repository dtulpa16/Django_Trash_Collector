from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns
# TODO: customer details,suspend,set up one time pick-up, payment(bonus)

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/',views.create, name = 'create'),
    path('update_pickup/', views.update_pickup, name = 'update_pickup'),
]

