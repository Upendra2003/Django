from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

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

def publish(request):
    form=ProjectForm()
    if request.method=='POST':
        form=ProjectForm(data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    context={
        'form':form,
    }
    return render(request,'projects/add-project.html',context)

