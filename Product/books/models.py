from django.db import models
from sympy import true

class Category(models.Model):
    # category_id = models.AutoField(primary_key=True)
    # category_id = models.CharField(max_length=7, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    des = models.TextField(null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    # book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/books/', null= True)
    price = models.FloatField()
    sale = models.FloatField()
    type = models.CharField(max_length=50, default='book')
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    des = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title