# from trash_collector.customers.models import Customer
from . import models
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.apps import apps
from datetime import datetime
from datetime import date
from .models import Employee
import calendar


# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')
    user = request.user
    try:
        logged_in_employee = Employee.objects.get(user=user)
    except:
        return HttpResponseRedirect(reverse('employees:create'))
    # return render(request, 'employees/index.html')

def todays_pickups(request):
    user = request.user
    logged_in_employee = Employee.objects.get(user=user)
    Customer = apps.get_model('customers.Customer')
    today = date.today()
    string_weekday = calendar.day_name[today.weekday()]
    customers = Customer.objects.filter(one_time_pickup=today, weekly_pickup = string_weekday)
    for pick_ups in customers:
        if pick_ups.one_time_pickup == today or pick_ups.weekly_pickup == calendar.day_name[today.weekday()] and logged_in_employee.zip_code == pick_ups.zip_code:
            context = {
                'customers' : customers
                }
            return render(request, 'employees/todays_pickups.html', context)

def create(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            zip_code = request.POST.get('zip_code')
            new_user = Employee(zip_code = zip_code, name = name, user = request.user)
            new_user.save()
            return render(request, 'employees/index.html')
        else:
            return render(request, 'employees/create.html')


