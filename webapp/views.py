from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from webapp.models import Order, Client, Tag, Product
from .forms import OrderForm, CreateUserForm, CustomerForm
#from webapp.filters import OrderFilter
from .users import unauthenticated_user, allowed_users, admin_only

# Create your views here.
def home(request):
    return render(request, 'webapp/index.html')

def dashboard(request):
	orders = Order.objects.all()
	clients = Client.objects.all()

	total_customers = clients.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'clients':clients,
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

def client(request, pk_test):
    client = Client.objects.get(id=pk_test)
    orders=client.order_set.all()
    order_count=orders.count()
    context={'client':client,'orders':orders,'order_count':order_count}
    return render(request, 'webapp/client.html', context)




def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'webapp/order_form.html', context)

def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'wepabb/order_form.html', context)

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'webapp/delete.html', context)

#@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			username = form.save()
			username = form.cleaned_data.get('username')


			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'webapp/register.html', context)
