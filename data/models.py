from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Register your models here.


class Data(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.PROTECT)
    title = models.CharField(max_length=100,unique=True,blank=False)
    Description = models.CharField(max_length=500,blank=False)
    File = models.FileField(upload_to="file/",max_length=250,null=True,default=None)
    
    def __str__(self):
        return str(self.id)