from django.db import models

# Create your models here.


class TodoItem(models.Model):
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.TextField(max_length=100)
