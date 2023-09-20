from django.db import models
import uuid

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    email=models.CharField(max_length=500,null=True,blank=True)
    phone=models.CharField(max_length=10,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    student_id=models.UUIDField(default=uuid.uuid4,null=False,primary_key=True)
    branch=models.ForeignKey('Branch',on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        ordering=['name']

    def __str__(self):
        return self.name
    
class Branch(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    branch_id=models.UUIDField(default=uuid.uuid4,null=False,primary_key=True)

    def __str__(self):
        return self.name
