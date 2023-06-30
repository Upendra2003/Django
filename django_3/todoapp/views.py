from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as login_user,logout as logout_user
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import TodoForm
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user=request.user
        form = TodoForm()
        todos=Task.objects.filter(user=user)
        context={
            'form':form,
            'todos':todos
        }
        return render(request,'todoapp/index.html',context)

def register(request):
    if request.method=='GET':
        form = UserCreationForm()
        context={
            'form':form
        }
        return render(request,'todoapp/register.html',context)
    else:
        form=UserCreationForm(request.POST)
        context={
            'form':form
        }
        if form.is_valid():
            user=form.save()
            if user is not None:
                return redirect('home')
        else:
            return render(request,'todoapp/register.html',context)

def login(request):
    if request.method=='GET':
        form = AuthenticationForm()
        context={
            'form':form
        }
        return render(request,'todoapp/login.html',context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login_user(request,user)
                return redirect('home')
        else:
            context={
                'form':form
            }
            return render(request,'todoapp/login.html',context)
        
def add_todo(request):
    if request.user.is_authenticated:
        user=request.user
        form=TodoForm(request.POST)
        if form.is_valid():
            todo=form.save(commit=False)
            todo.user=user
            todo.save()
            return redirect('home')
        else:
            return render(request,'index.html',context={'form':form})
        

def delete_todo(request,id):
    Task.objects.get(pk=id).delete()
    return redirect('home')


def logout(request):
    logout_user(request)
    return redirect('login')