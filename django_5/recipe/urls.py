from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add_recipe',views.add_recipe,name='add-recipe'),
    path('show_recipes',views.show_recipes,name='show-recipes'),
    path('search_recipe',views.search_recipe,name='search-recipe'),
    path('view_recipe/<int:id>',views.view_recipe,name='view-recipe'),
    path('update_recipe/<int:id>',views.update_recipe,name='update-recipe'),
    path('delete_recipe/<int:id>',views.delete_recipe,name='delete-recipe'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
]
