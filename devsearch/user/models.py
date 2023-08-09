from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(max_length=200,null=True,blank=True)
    short_desc=models.CharField(max_length=200,null=True,blank=True)
    bio=models.TextField(max_length=300,null=True,blank=True)
    profile_img=models.ImageField(null=True,blank=True,upload_to='profiles/',default='spline.jpg')
    linkedin_link=models.CharField(max_length=200,null=True,blank=True)
    github_link=models.CharField(max_length=200,null=True,blank=True)
    instagram_link=models.CharField(max_length=200,null=True,blank=True)
    twitter_link=models.CharField(max_length=200,null=True,blank=True)
    p_id=models.UUIDField(default=uuid.uuid4,null=True,blank=True)

    def __str__(self):
        return str(self.user.username)
    
