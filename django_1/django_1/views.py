from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    text=request.GET.get('text','default')
    remove_punctuation=request.GET.get('remove_punctuation','off')
    capitalize_text=request.GET.get('capitalize_text','off')
    print(remove_punctuation)
    if remove_punctuation=='on':
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed_text=''
        for char in text:
            if char not in punctuations:
                analyzed_text+=char
        result={'analyzed_text':analyzed_text,'operation':'Removed Punctuation'}
        return render(request,'analyze.html',result)
    elif capitalize_text=='on':
        analyzed_text=text.upper()
        result={'analyzed_text':analyzed_text,'operation':'Upper case'}
        return render(request,'analyze.html',result)
    return '404'