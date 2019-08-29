import datetime

from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=30)

class Product(models.Model):
    title = models.CharField(max_length=30)
    image = models.CharField(max_length=200)
    price = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    # question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Product, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
