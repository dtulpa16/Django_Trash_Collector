from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns
# TODO: employee details,daily houses,
# TODO: index page for employees will show customers in zipcode and non-suspended accounts
# TODO: add button to index page that will charge the custer and change Pickup_status model to true

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/',views.create, name = 'create'),
    path('todays_pickups/', views.todays_pickups, name = 'todays_pickups'),
    path('charge_customer/<int:charge>/', views.charge_customer, name= 'charge_customer'),
    path('filter/<str:day_of_week>/', views.filter, name = 'filter'),
    path('search_by_day/', views.search_by_day, name = 'search_by_day')
]