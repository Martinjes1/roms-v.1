from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib import messages
from .models import *
from .forms import OrderForm, CustomerForm, CreateUserForm, addProductForm

@login_required(login_url='login')
def registerPage(request):
			form=CreateUserForm()
			if request.method == 'POST':
				form = CreateUserForm(request.POST)
				if form.is_valid():
					form.save()
					user = form.cleaned_data.get('username')
					messages.success(request, 'Account was Created for '+ user)
					return redirect('login')
			context = {'form': form}
			return render(request, 'accounts/register.html', context)

def loginPage(request):
	
			if request.method == 'POST':
				username=request.POST.get('username')
				password=request.POST.get('password')
				user = authenticate(request, username=username, password=password)
				if user is not None:
					login(request, user)
					return redirect('home')	
				else:
					messages.info(request, 'Username Or Password is incorrect')
			context = {}
			return render(request, 'accounts/login.html', context)

def logoutPage(request):
	logout(request)
	return redirect('home')


def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()
	total_customers = customers.count()
	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()
	outof_delivery = orders.filter(status='Out for delivery').count()
	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending, 'outof_delivery':outof_delivery}
	if request.user.is_authenticated:
		return render(request, 'accounts/dashboard.html', context)
	else:
		return render(request, 'accounts/user_dashboard.html', context)

def products(request):
	products = Product.objects.all()
	if request.user.is_authenticated:
		return render(request, 'accounts/products.html', {'products':products, 'title':'Products'})
	else:
		return render(request, 'accounts/user_products.html', {'products':products, 'title':'Products'})
	

@login_required(login_url='login')
def addProducts(request):
	Product_Form = addProductForm()
	if request.method == 'POST':
		Product_Form = addProductForm(request.POST)
		if Product_Form.is_valid():
			Product_Form.save()
			return redirect('products')
	context = {
		'Product_Form':Product_Form, 'title': 'Add Products'
	}
	return render(request, 'accounts/add_products.html', context)

@login_required(login_url='login')
def deleteProduct(request, pk):
	product = Product.objects.get(id=pk)
	if request.method == "POST":
		product.delete()
		return redirect('products')
	context = {'item':product, 'title': 'Delete Product'}
	return render(request, 'accounts/delete_product.html', context)



@login_required(login_url='login')
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)
	orders = customer.order_set.all()
	order_count = orders.count()
	context = {'customer':customer, 'orders':orders, 'order_count':order_count, 'title':'Customer'}
	return render(request, 'accounts/customer.html',context)


def all_customer(request):
	customers = Customer.objects.all()
	total_customers = customers.count()
	context ={
		'customers':customers, 'total_customers':total_customers, 'title':'All Customer'
	}
	if request.user.is_authenticated:
		return render(request, 'accounts/all_customer.html', context)
	else:
		return render(request, 'accounts/user_all_customer.html', context)


@login_required(login_url='login')
def createCustomer(request):
	Customer_form = CustomerForm()
	if request.method == 'POST':
		Customer_form = CustomerForm(request.POST)
		if Customer_form.is_valid():
			Customer_form.save()
			return redirect('allcustomer')
	context = {'Customer_form':Customer_form, 'title': 'Create Customer'}
	return render(request, 'accounts/customer_form.html', context)

@login_required(login_url='login')
def UpdateCustomer(request, pk):
	customer = Customer.objects.get(id=pk)
	Customer_form = CustomerForm(instance=customer)
	if request.method == 'POST':
		Customer_form = CustomerForm(request.POST, instance=customer)
		if Customer_form.is_valid():
			Customer_form.save()
			return redirect('allcustomer')
	context = {'Customer_form':Customer_form, 'title':'Update Customer'}
	return render(request, 'accounts/customer_form.html', context)

@login_required(login_url='login')
def deleteCustomer(request, pk):
	customer = Customer.objects.get(id=pk)
	if request.method == "POST":
		customer.delete()
		return redirect('/')
	context = {'item':customer, 'title': 'Delete Customer'}
	return render(request, 'accounts/delete_customer.html', context)

@login_required(login_url='login')
def createOrder(request, pk):
	customer = Customer.objects.get(id=pk)
	form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form, 'title': 'Create Order'}
	return render(request, 'accounts/order_form.html', context, )

@login_required(login_url='login')
def updateOrder(request, pk):
	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)
	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form, 'title': 'Update Order'}
	return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')
	context = {'item':order, 'title':'Delete Order'}
	return render(request, 'accounts/delete_order.html', context)