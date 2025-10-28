from turtle import Vec2D

from django.db import models

class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=100)
    unit_price=models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.product_name
