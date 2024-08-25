from django.shortcuts import render, redirect
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

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
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")  
    else:
        form = UserCreationForm()  

    # Render the template with the form
    return render(request, "Signup.html", {"form": form })