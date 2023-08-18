from django.shortcuts import render,redirect
from user.models import Profile
from projects.models import Project
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.models import User
from projects.views import home
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        try:
            user=User.objects.all(username=username)
        except:
            messages.error(request,"User Doesn't Exist")

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"invalid credentials")

    return render(request,'user/user-login.html')

def logout_page(request):
    logout(request)
    messages.add_message(request,messages.INFO,"User logged out")
    return redirect('login')

def register_page(request):
    useremail=request.POST.get('useremail')
    if request.method=='POST':
        user=User.objects.create(
            username=request.POST.get('username'),
            email=request.POST.get('useremail'),
        )
        user.set_password(request.POST.get('password'))
        user.save()
        return redirect('login')

    return render(request,'user/register-page.html')

# Create your views here.
@login_required(login_url='login')
def user(request):
    all_profiles=Profile.objects.all()
    context={
        'all_profiles':all_profiles
    }
    return render(request,'user/user-profiles.html',context)

@login_required(login_url='login')
def profile(request,id):
    get_profile=Profile.objects.get(p_id=id)
    get_projects=get_profile.project_set.all()
    context={
        'get_profile':get_profile,
        'get_projects':get_projects
    }
    return render(request,'user/profile.html',context)

@login_required(login_url='login')
def user_profile(request):
    profile=request.user.profile
    context={
        'profile':profile
    }
    return render(request,'user/user-profile.html',context)

@login_required(login_url='login')
def edit_profile(request):
    profile=request.user.profile
    if request.method=='POST':
        profile.name=request.POST.get('username')
        profile.email=request.POST.get('email')
        profile.short_desc=request.POST.get('short_desc')
        profile.profile_img=request.FILES.get('profile-img')
        profile.linkedin_link=request.POST.get('linkedinlink')
        profile.github_link=request.POST.get('gitlink')
        profile.instagram_link=request.POST.get('instagramlink')
        profile.bio=request.POST.get('bio')
        profile.save()
    return redirect('user-profile')