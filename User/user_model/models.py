# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
# This is our model for user registration.
class User(AbstractUser):
### The following are the fields of our table.
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    mobile = models.CharField(max_length=12)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=200)
    
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['fname','lname','mobile'] 
### It will help to print the values.
def __str__(self):
    return self.email

    