from django.http import HttpResponse
from django.shortcuts import render

def index(Response):
    return render(Response,'index.html')