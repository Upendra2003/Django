from django.shortcuts import render
from django.http import HttpResponse
from user.models import Profile
from projects.models import Project

# Create your views here.
def user(request):
    all_profiles=Profile.objects.all()
    context={
        'all_profiles':all_profiles
    }
    return render(request,'user/user-profiles.html',context)

def profile(request,id):
    get_profile=Profile.objects.get(p_id=id)
    get_projects=get_profile.project_set.all()
    context={
        'get_profile':get_profile,
        'get_projects':get_projects
    }
    return render(request,'user/profile.html',context)