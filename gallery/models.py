# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import dt

# Create your models here.


class Image(models.Model):
    post = models.TextField()
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    def __str__(self):
      return self.name


class Category(models.Model):
  category=models.CharField(max_length=30)

  def __str__(self):
    return self.category

class Location(models.Model):
  location=models.CharField(max_length=30)

  def __str__(self):
    return self.location