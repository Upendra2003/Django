from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Recipe

# Create your views here.
def home(request):
    return render(request,'recipe/index.html')

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
    
def show_recipes(request):
    all_recipes=Recipe.objects.all()
    context={
        "all_recipes":all_recipes
    }
    return render(request,'recipe/recipes.html',context)