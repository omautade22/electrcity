from django.db import models

# Create your models here.
class User(models.Model):
    #id
    username = models.CharField('User name',max_length=50)
    email = models.CharField('User email', max_length=50)
    password = models.CharField('User Password', max_length=20)
