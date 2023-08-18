
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('register/',views.register_page,name='register'),

    path('',views.user,name='user'),
    path('profile/<str:id>',views.profile,name='profile'),
    path('user-profile/',views.user_profile,name='user-profile'),

    path('edit-profile/',views.edit_profile,name='edit-profile')
]
