from django.db import models

# Create your models here.

class destinations(models.Model):

    name = models.CharField(max_length = 100, default = '')
    img = models.ImageField(upload_to = 'pics', default = '')
    descp = models.TextField(default = '')
    price = models.IntegerField(default = '')
    offer = models.BooleanField(default = False)