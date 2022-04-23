from django.db import models

# Create your models here.

class Data(models.Model):
    title = models.CharField(max_length=100,unique=True,blank=False, verbose_name="Title")
    Description = models.CharField(max_length=500,blank=False)
    File = models.FileField(upload_to="file/",max_length=250,null=True,default=None)
    

    def __str__(self):
        return self.title