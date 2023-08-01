from django.shortcuts import render
from django.http import HttpResponse
from .models import Project,Tag

# Create your views here.
def home(request):
    projects=Project.objects.all()
    context={
        'projects':projects
    }
    return render(request,'projects/index.html',context)

def project(request,id):
    project=Project.objects.get(pk=id)
    tags=project.tags.all()
    context={
        'project':project,
        'tags':tags
    }
    return render(request,'projects/projects.html',context)