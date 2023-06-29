from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50,default='')
    product_description=models.CharField(max_length=100,default='')
    product_price=models.IntegerField(default=0)
    product_image=models.ImageField(upload_to='shop/images',default='')
    product_category=models.CharField(max_length=100,default='')
    pub_date=models.DateField()

    def __str__(self):
        return self.product_name