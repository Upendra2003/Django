from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    p_id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    project_name=models.CharField(max_length=200)
    project_desc=models.TextField(max_length=1000,null=True,blank=True)
    # user
    project_image=models.ImageField(null=True,blank=True,default='default.png')
    tags=models.ManyToManyField('Tag')
    star=models.BooleanField(null=True,blank=True)
    created=models.DateField(auto_now_add=True)
    link=models.CharField(max_length=2000,null=True,blank=True)
    source_code=models.CharField(max_length=2000,null=True,blank=True)
    
    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.project_name
    

class Tag(models.Model):
    tag_id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    tag_name=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.tag_name
