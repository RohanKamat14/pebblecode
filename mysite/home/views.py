from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib import messages
from .models import Product
from .forms import SignupUserForm
from .cart import Cart
from django.http import JsonResponse

def index(request):
    template = loader.get_template('index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def Signup(request): 
    if request.method == "POST":
        form = SignupUserForm(request.POST)
        if form.is_valid():
            auth_login(request, form.save())
            return redirect("index")  
    else:
        form = SignupUserForm() 

    return render(request, "Signup.html", {"form": form })

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))
            return redirect('login')
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
    
def courses_view(request):
    courses_list = Product.objects.all()
    return render(request, 'courses.html', {'courses_list':courses_list})

def show_courses(request, courses_id):   
    courses = Product.objects.get(pk=courses_id)
    return render(request, 'show_courses.html', {'courses':courses})

def my_courses(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    return render(request, "my_courses.html", {"cart_products":cart_products})

def my_add(request):
    #get the cart
    course = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        course.add(product=product)

        course_quantity = len(course)

        response = JsonResponse({'qty': course_quantity})
        return response

def my_delete():
    pass

def my_update():
    pass