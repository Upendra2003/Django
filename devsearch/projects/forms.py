from django.forms import ModelForm,widgets
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model=Project
        fields=['project_name','project_desc','project_image','tags','link','source_code']
        widgets={
            'project_name': forms.TextInput(attrs={'class':'form-control'}),
            'project_desc': forms.TextInput(attrs={'class':'form-control'}),
            'project_image': forms.FileInput(attrs={'class':'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class':'form-control'}),
            'link': forms.TextInput(attrs={'class':'form-control'}),
            'source_code': forms.TextInput(attrs={'class':'form-control'}),
        }