from builtins import object
from django.shortcuts import redirect, render
from .models import Customer, Pledging
# Create your views here.

def my_login(request):
    return render(request, template_name='login.html')

def pledging(request):
    pledging = Pledging.objects.all()
    return render(request, 'pledging.html', context={'pledging': pledging})

def customers(request):
    customer = Customer.objects.all()
    return render(request, 'customers.html', context={'customer': customer})

def view_customer(request, cus_id):
    view_cus = Customer.objects.get(pk=cus_id)
    return render(request, 'view_customer.html', context={'cus': view_cus})

def view_pledging(request, pled_id):
    view_pled = Pledging.objects.get(pk=pled_id)
    return render(request, 'view_pledging.html', context={'p': view_pled})