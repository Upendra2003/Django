from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as login_user,logout as logout_user
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,'recipe/index.html')

@login_required(login_url='login')
def add_recipe(request):
    if request.method=='POST':
        print(request.FILES.get('recipe-image'))
        new_recipe=Recipe.objects.create(
            recipe_title=request.POST.get('recipe-title'),
            recipe_description=request.POST.get('recipe-description'),
            recipe_image=request.FILES.get('recipe-image')
        )
        new_recipe.save()
        return redirect(home)
    else:
        return render(request,'recipe/index.html',context={"error":"Error Occured"})

@login_required(login_url='login')
def show_recipes(request):
    all_recipes=Recipe.objects.all()
    context={
        "all_recipes":all_recipes
    }
    return render(request,'recipe/recipes.html',context)

@login_required(login_url='login')
def search_recipe(request):
    if request.method=='POST':
        get_recipe=Recipe.objects.filter(recipe_title__icontains=request.POST.get('search-recipe')).all()
        context={
            'get_recipe':get_recipe,
            'status':True
        }
        return render(request,'recipe/search.html',context)
    return redirect(show_recipes)

@login_required(login_url='login')
def view_recipe(request,id):
    get_recipe=Recipe.objects.get(pk=id)
    context={
            'get_recipe':get_recipe,
        }
    return render(request,'recipe/view_recipe.html',context)

@login_required(login_url='login')
def update_recipe(request,id):
    get_recipe=Recipe.objects.get(id=id)
    if request.method=='POST':
        get_recipe.recipe_title=request.POST.get('recipe-title')
        get_recipe.recipe_description=request.POST.get('recipe-description')
        get_recipe.recipe_image=request.FILES.get('recipe-image')
        get_recipe.save()
        return redirect(show_recipes)
    context={
        "get_recipe":get_recipe
    }
    return render(request,'recipe/update.html',context)

@login_required(login_url='login')
def delete_recipe(request,id):
    Recipe.objects.get(id=id).delete()
    return redirect(show_recipes)

def register(request):
    if request.method=='POST':
        user = User.objects.create(
            username=request.POST.get('username'),
            email=request.POST.get('email')
        )
        user.set_password(request.POST.get('password'))
        user.save()
    return render(request,'recipe/register.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if not User.objects.filter(username=username):
            messages.error(request,"username doenst exist")
            return redirect(login)
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,"invalid credentials")
            return redirect(login)
        else:
            login_user(request,user)
            return redirect(home)
    return render(request,'recipe/login.html')

def logout(request):
    logout_user(request)
    return redirect(login)