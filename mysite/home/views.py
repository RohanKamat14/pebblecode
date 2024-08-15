from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse


def index(request):
    template = loader.get_template('index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def courses(request):
    template = loader.get_template('courses.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('login.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
def Signup(request):
    template = loader.get_template('Signup.html')
    context = {

    }
    return HttpResponse(template.render(context, request))