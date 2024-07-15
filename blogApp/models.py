from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    description=models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
 