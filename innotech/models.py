from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Product(models.Model):
    #Title
    #Image
    #Summary/Details

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    summary = RichTextField()

class About(models.Model):
    summary = RichTextField()


class Slider(models.Model):
    image = models.ImageField(upload_to='images/')

class Media(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    summary =models.TextField(max_length=50)
