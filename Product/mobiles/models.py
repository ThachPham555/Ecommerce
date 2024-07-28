from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    des = models.TextField(null=True)

    def __str__(self):
        return self.name

class Mobile(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/mobiles/')
    price = models.FloatField()
    sale = models.FloatField()
    type = models.CharField(max_length=50, default='mobile')
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    des = models.TextField(null=True)
    brand = models.ForeignKey(Brand(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title