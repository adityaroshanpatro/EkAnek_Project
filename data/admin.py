from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline, register
from .models import Data

# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'Description','File']
    list_display_links = ('id','title')
    search_fields = ('title','File')
admin.site.register(Data,DataAdmin)