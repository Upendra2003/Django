from django.shortcuts import render
from .models import Product

# Create your views here.
def index(req):
    get_category=Product.objects.values('product_category','product_id')
    all_cats={item['product_category'] for item in get_category}
    for category in all_cats:
        all_products=Product.objects.filter(product_category=category).values()
    list(all_products)
    # for i,j in all_products:
    #     print(i,j)
    print(all_products)
    context={
        "data":all_products,
    }
    return render(req,'shop/index.html',context)