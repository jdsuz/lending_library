from django import forms 

from .models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['text', 'product_type', 'description', 'borrower']
		labels = {'text': ''}

class BorrowProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['text', 'product_type', 'description']