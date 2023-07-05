from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add_recipe',views.add_recipe,name='add-recipe'),
    path('show_recipes',views.show_recipes,name='show-recipes')
]
