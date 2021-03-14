from django.db import models
from datetime import datetime
from main.choices import *

# Create your models here.

class Blog(models.Model): #blog
    blog_title = models.CharField(max_length=200)
    blog_content = models.TextField()
    blog_published = models.DateTimeField('date published')

    def __str__(self):
        return self.blog_title

class Phone(models.Model): #phone
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class KeyVal(models.Model): #values
    container = models.ForeignKey(Phone, db_index=True, on_delete=models.CASCADE)
    year = models.CharField(max_length=240, db_index=True)
    price = models.CharField(max_length=240, db_index=True)

    def __str__(self):
        return str(self.container)+'{'+str(self.year)+'}'