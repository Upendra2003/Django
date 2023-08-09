
from django.urls import path
from . import views

urlpatterns = [
    path('',views.user,name='user'),
    path('profile/<str:id>',views.profile,name='profile')
]
