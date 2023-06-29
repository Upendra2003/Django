from django.shortcuts import render
from .models import Product

# Create your views here.
def index(req):
    get_data=Product.objects.all()
    get_category=Product.objects.values_list('product_category')
    get_len=len(get_data)
    context={
        # "category":get_category,
        "data":get_data,
        # "length":get_len
    }
    return render(req,'shop/index.html',context)