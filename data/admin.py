from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline, register
from .models import Data
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Register your models here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from data.models import Data





class DataAdmin(admin.ModelAdmin):
    # readonly_fields = ['user']
    list_display = ['id', 'title', 'Description','File','user']
    list_display_links = ('id','title')
    search_fields = ('title','File')
    
    def user(request):
        print("lyykykyk")
        return 
    
    def save(request):
        users = Data.objects.filter(user=request.user)
        print("Llllllllllllllllllllllllllllllllllllllllllllllllll")
        return render(request,  {'data' : users})



admin.site.register(Data,DataAdmin)