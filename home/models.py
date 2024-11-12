from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    desc=models.TextField()
    
    def __str__(self):
        return self.name