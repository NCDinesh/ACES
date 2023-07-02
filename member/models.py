from django.db import models

class member(models.Model):
    name = models.CharField( max_length=50)
    email=models.EmailField(max_length=254)
    message = models.CharField( max_length=250)

# Create your models here.
