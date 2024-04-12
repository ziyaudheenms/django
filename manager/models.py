from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Passwords(models.Model):
    Account_Name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=8)
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.username