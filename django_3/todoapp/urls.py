from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('add-todo/',views.add_todo,name='add_todo'),
    path('logout/',views.logout,name='logout'),
    path('delete-todo/<int:id>',views.delete_todo,name='delete_todo')
]
