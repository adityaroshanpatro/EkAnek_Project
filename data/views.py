from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from data.models import Data
# Create your views here.

def index(request):
    
    return render(request, 'data/index.html')

def about(request):
    ls = Data.objects.get(id=id)
    if ls in request.user.title.all():
        if request.method == "POST":
            print("1111111111111111111111")
            return render(request, 'data/about.html')