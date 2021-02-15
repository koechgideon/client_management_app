from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from webapp.models import Order, Customer, Tag, Product
from .forms import OrderForm, CreateUserForm, CustomerForm
#from webapp.filters import OrderFilter
from .users import unauthenticated_user, allowed_users, admin_only

# Create your views here.
def home(request):
    return render(request, 'webapp/index.html')

def dashboard(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	#total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }

	return render(request, 'webapp/dashboard.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('dashboard')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'webapp/login.html', context)

def products(request):
	products = Product.objects.all()

	return render(request, 'webapp/products.html', {'products':products})

def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders=customer.order_set.all()
    order_count=orders.count()
    context={'customer':customer,'orders':orders,'order_count':order_count}
    return render(request, 'webapp/customer.html', context)
