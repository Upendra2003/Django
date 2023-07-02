from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('all_products/',views.all_product,name='all_product'),
    path('view_product/<int:id>',views.view_product,name='view_product')
]