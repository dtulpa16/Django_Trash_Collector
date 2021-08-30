# from trash_collector.customers.models import Customer
from . import models
from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps
from datetime import date
from .models import Employee

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')

def todays_pickups(request):
    Customer = apps.get_model('customers.Customer')
    today = date.today()
    customers = Customer.objects.filter(one_time_pickup=today)
    for pick_ups in customers:
        if pick_ups.one_time_pickup == today:
            context = {
                'customers' : customers
                }
            return render(request, 'employees/todays_pickups.html', context)


