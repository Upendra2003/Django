from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add_recipe',views.add_recipe,name='add-recipe'),
    path('show_recipes',views.show_recipes,name='show-recipes'),
    path('search_recipe',views.search_recipe,name='search-recipe'),
    path('view_recipe/<int:id>',views.view_recipe,name='view-recipe'),
]
