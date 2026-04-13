from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    msg=models.CharField(max_length=500)

    def __str__(self):
        return self.name