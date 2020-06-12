from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def index(request):
    users = {'user_name': 'Lakshmi'}
    return render(request,'sampleapp/index.html',context=users)
    # return HttpResponse("Miss you Mom",status=200)
