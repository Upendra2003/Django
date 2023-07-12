from django.contrib import admin
from .models import Branch,Student,Subjects

# Register your models here.
admin.site.register(Branch)
admin.site.register(Student)
admin.site.register(Subjects)