from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required(login_url='login')
def home(request):
    search_query=''
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')
    projects=Project.objects.filter(
        Q(project_name__icontains=search_query) | Q(project_desc__icontains=search_query) | Q(tags__tag_name__icontains=search_query)
    )
    context={
        'projects':projects,
        'search_query':search_query
    }
    return render(request,'projects/index.html',context)


@login_required(login_url='login')
def project(request,id):
    project=Project.objects.get(pk=id)
    tags=project.tags.all()
    context={
        'project':project,
        'tags':tags
    }
    return render(request,'projects/projects.html',context)


@login_required(login_url='login')
def publish(request):
    profile=request.user.profile
    form=ProjectForm()
    if request.method=='POST':
        form=ProjectForm(data=request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
        return redirect('home')
    context={
        'form':form,
    }
    return render(request,'projects/add-project.html',context)

