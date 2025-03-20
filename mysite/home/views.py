from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib import messages
from .models import Product, Category,Lesson,Page, Quiz, Question, Answer, Test, TestAnswer, TestQuestion
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

def category(request, cat):
    cat = cat.replace('-', ' ')
    # Grab the category from the url
    try:
        category = Category.objects.get(name=cat)
        courses = Product.objects.filter(category=category)
        return render(request, 'category.html', {'courses_list':courses,  'category':category})
    except:
        messages.success(request, ("That category dosn't exist"))
        return redirect('index')

def show_courses(request, courses_id):   
    courses = Product.objects.get(pk=courses_id)
    lessons = courses.lessons.all()
    return render(request, 'show_courses.html', {'courses':courses, 'lessons': lessons})

def lesson_view(request, product_id):
    lesson = get_object_or_404(Lesson, id=product_id)
    pages = lesson.pages.all()
    first_page = pages.first() if pages.exists() else None
    return render(request, 'lesson.html', {'lesson':lesson, 'pages': pages, 'first_page': first_page})

def page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    related_pages = Page.objects.filter(lesson=page.lesson).order_by('id')

    page_list = list(related_pages)
    total_pages = len(page_list)
    current_index = page_list.index(page) + 1 if page in page_list else 1
    prev_page = page_list[current_index - 2] if current_index > 1 else None
    next_page = page_list[current_index] if current_index < total_pages else None

    
    quiz = Quiz.objects.filter(lesson=page.lesson).first()  

    return render(request, "page.html", {
        'page': page,
        'prev_page': prev_page,
        'next_page': next_page,
        'current_index': current_index,
        'total_pages': total_pages,
        'quiz': quiz if current_index == total_pages else None  
    })

def quiz_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()  
    current_lesson = quiz.lesson  

    if request.method == "POST":
        total_questions = questions.count()
        wrong_answers = 0
        wrong_question_ids = []  

        for question in questions:
            user_answer_id = request.POST.get(f'question_{question.id}')
            correct_answer = question.answers.filter(is_correct=True).first()
            
            if user_answer_id and correct_answer:
                if user_answer_id != str(correct_answer.id):  
                    wrong_answers += 1
                    wrong_question_ids.append(question.id)

        score = total_questions - wrong_answers

       
        next_lesson = Lesson.objects.filter(id__gt=current_lesson.id).order_by('id').first()
        
        return render(request, 'quiz_result.html', {
            "quiz": quiz,
            'questions': questions,
            'wrong_answers': wrong_answers,
            'score': score,
            'wrong_question_ids': wrong_question_ids,
            'next_lesson': next_lesson  
        })

    return render(request, "quiz.html", {
        'quiz': quiz,
        'questions': questions,
    })

def test_view(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = Test.objects.filter()
    
    if request.method == 'POST':
        total_questions = questions.count()
        wrong_answers = 0
        wrong_question_ids = []

        for question in questions:
            user_answer_id = request.POST.get((f'question_{question.id}'))
            correct_answer = question.answers.filter(is_correct =True).first()

            if user_answer_id and correct_answer:
                if user_answer_id != str(correct_answer.id):
                    wrong_answers += 1
                    wrong_question_ids.append(question.id)
    
        score = total_questions - wrong_answers

        return render(request, 'quiz_result.html', {
            "test": test,
            'questions': questions,
            'wrong_answers': wrong_answers,
            'score': score,
            'wrong_question_ids': wrong_question_ids
        })

    return render(request, "test.html", {
        'test': test,
        'questions': questions,

    })

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