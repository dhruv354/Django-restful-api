from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=35)
    author = models.CharField(max_length=35)
    email = models.EmailField(max_length=20)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title