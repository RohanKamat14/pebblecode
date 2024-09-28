from django.shortcuts import render, redirect
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout
from .models import Product

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

def Signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            auth_login(request, form.save())
            return redirect("index")  
    else:
        form = UserCreationForm()  

    # Render the template with the form
    return render(request, "Signup.html", {"form": form })

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #Login here
            auth_login(request, form.get_user())
            return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form })
    
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("index")
    
def search_courses(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        courses = Product.objects.filter(name__contains=searched)
        return render(request, 'search_courses.html', {'searched':searched, 'courses' : courses})
    else:
        return render(request, 'search_courses.html', {})