from django.db import models

# Create your models here.
from django.db import models


class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name


class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    created_at = models.DateField(auto_now=True)
    delivery_date = models.DateField()