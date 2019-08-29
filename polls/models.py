import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=30) 
    name = models.CharField(max_length=30)

class Product(models.Model):
    title = models.CharField(max_length=30, default='unsee')
    image = models.CharField(max_length=200, default='unsee')
    price = models.CharField(max_length=30, default='unsee')
    description = models.CharField(max_length=200, default='unsee')
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)
    # question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Command(models.Model):
    login = models.CharField(max_length=30) 
    basket = models.CharField(max_length=30)
    date = models.DateTimeField('date published')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Choice(models.Model):
    question = models.ForeignKey(Product, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
