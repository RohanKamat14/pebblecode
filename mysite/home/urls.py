from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("courses", views.courses, name='courses'),
    path("login", views.login_view, name='login'),
    path("Signup", views.Signup, name = 'Signup'),
    path("logout", views.logout_view, name = 'logout'),
    path("search_courses", views.search_courses, name = 'search_courses')
]