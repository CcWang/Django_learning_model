# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from .models import Interest,User
def index(request):
    
  return render(request,'interests/index.html')
