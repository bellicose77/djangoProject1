from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    dict={'text1':'The text is sent from views'}
    return render(request,'My_firstapp/index.html',context=dict)


def home(request):
    return HttpResponse("<h1>I am from the firstapp</h1>")

def about(request):
    return HttpResponse("this is the about")

def contact(request):
    return HttpResponse("Please contact us")
