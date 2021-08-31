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
    path('filter/<str:day>/', views.filter, name = 'filter'),
]