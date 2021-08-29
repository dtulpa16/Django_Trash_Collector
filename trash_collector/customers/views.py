
from django.shortcuts import render
from .models import Customer
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user

    try:
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
        logged_in_customer = Customer.objects.get(user=user)
    except:
        # TODO: Redirect the user to a 'create' function to finish the registration process if no customer record found
        return HttpResponseRedirect(reverse('customers:create'))
        

    # It will be necessary while creating a Customer/Employee to assign request.user as the user foreign key

    print(user)
    return render(request, 'customers/index.html')

def create(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            address = request.POST.get('address')
            zip_code = request.POST.get('zip_code')
            weekly_pickup = request.POST.get('weekly_pickup')
            new_user = Customer(name= name, zip_code = zip_code, address = address, weekly_pickup = weekly_pickup)
            new_user.save()
            return render(request, 'customers/index.html')
        else:
            return render(request, 'customers/create.html')
