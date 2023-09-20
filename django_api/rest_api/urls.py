from django.urls import path
from . import views

urlpatterns = [
    path('get-student-details/', views.get_details,name='get-student-details'),
    path('add-student-details/', views.add_student,name='add-student-details'),
    path('edit-student-details/<str:id>', views.edit_student,name='edit-student-details'),
]