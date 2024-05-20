from django.http import HttpResponse
from django.shortcuts import render

def Homepage(req):
    # return HttpResponse("Hellp world")
    return render(req, 'home.html')

def Aboutpage(req):
    # return HttpResponse("just trying man")
    return render(req, 'about.html')