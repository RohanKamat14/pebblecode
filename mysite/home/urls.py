from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("courses", views.courses, name='courses'),
    path("login", views.login, name='login'),
    path("Signup", views.Signup, name = 'Signup')
]