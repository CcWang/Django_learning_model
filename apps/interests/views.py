# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from .models import Interest,User
def index(request):

  return render(request,'interests/index.html')
def show(request):
    users = User.objects.all()
    # for user in users:
    #     interest = Interest.objects.get()
    return render(request,'interests/show.html',{"users":users})
def user(request,user_id):
    try:
        user = User.objects.get(pk=user_id)

    except User.DoesNotExist:
        return HttpResponseNotFound
    else:
        user ={
            'user':user,

        }
    return render(request,'interests/user.html',user)
