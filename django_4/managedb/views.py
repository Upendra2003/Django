from django.shortcuts import render
from .forms import ProductForm
from .models import Product,Category

# Create your views here.
def home(request):
    if request.method=='POST':
        form=ProductForm(data=request.POST)
        if form.is_valid():
            context={
                'form':form
            }
            product=form.save()
            print(product)
            return render(request,'managedb/index.html',context)
    form=ProductForm()
    context={
        'form':form
    }
    return render(request,'managedb/index.html',context)

def all_product(request):
    all_categories=Category.objects.all()
    all_products=Product.objects.all()
    context={
        'all_products':all_products,
        'all_categories':all_categories
    }
    return render(request,'managedb/view.html',context)

def view_product(request,id):
    get_product=Product.objects.filter(pk=id)
    context={
        'get_product':get_product
    }
    return render(request,'managedb/view_product.html',context)

def collectionview(request,id):
    get_category=Category.objects.get(pk=id)
    print(get_category)
    get_products_by_collection=Product.objects.filter(product_category=get_category)
    context={
        'products':get_products_by_collection
    }
    return render(request,'managedb/collectionview.html',context)