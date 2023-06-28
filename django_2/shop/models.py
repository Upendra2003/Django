from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50,default='')
    product_description=models.CharField(max_length=100,default='default')
    pub_date=models.DateField()