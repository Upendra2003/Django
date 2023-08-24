from django.contrib import admin
from projects.models import Project,Tag,Review

# Register your models here.
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Review)