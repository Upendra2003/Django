from django.db import models

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=200)

    def __str__(self):
        return self.category
    
class Product(models.Model):
    produce_name=models.CharField(max_length=200)
    product_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.produce_name