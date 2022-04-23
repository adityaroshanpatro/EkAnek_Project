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
    list_display = ['id', 'title', 'Description','File','user']
    list_display_links = ('id','title')
    search_fields = ('title','File')
    
    @login_required
    def todos_for_user(request):
        users = Data.objects.filter(user=request.user)
        return render(request, 'templates/data/index.html', {'data' : users})



admin.site.register(Data,DataAdmin)