from django.db import models

# Create your models here.
class Branch(models.Model):
    branch=models.CharField(max_length=50)

    def __str__(self):
        return self.branch

class Subjects(models.Model):
    subject_name=models.CharField(max_length=100,null=True,blank=True)
    marks_obtained=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.subject_name

class Student(models.Model):
    student_name=models.CharField(max_length=100,null=True,blank=True)
    student_id=models.CharField(max_length=10,null=True,blank=True)
    student_branch=models.OneToOneField(Branch,on_delete=models.CASCADE,blank=True,null=True)
    student_subjects=models.ForeignKey(Subjects,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.student_name
    