from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
from data.utils import SaveModel
# Register your models here.


class Data(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,unique=True,blank=False)
    Description = models.CharField(max_length=500,blank=False)
    File = models.FileField(upload_to="file/",max_length=250,null=True,default=None)
    
    # def title(self, request, obj, *args, **kwargs):
    #     # data = Data.objects.create(user=request.user, tries=10, successful_tries=5)
    #     print("342545453666666666666666")
    #     # print(data)
    #     model_obj = SaveModel.title(self, request, obj)
    #     super().title(request, model_obj, *args, **kwargs)

    def __str__(self):
        return str(self.id)