from django.forms import ModelForm
from .models import *

class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields=['produce_name','product_category']
