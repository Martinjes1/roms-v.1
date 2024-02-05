from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Order, Customer, Product


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class addProductForm(ModelForm):
	class Meta:
		model = Product
		fields = [ 'name','category','price']
		