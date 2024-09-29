from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    #login/signup/logiut URL's
    path("login", views.login_view, name='login'),
    path("Signup", views.Signup, name = 'Signup'),
    path("logout", views.logout_view, name = 'logout'),

    #Courses URl's
    path("search_courses", views.search_courses, name = 'search_courses'),
    path("courses", views.courses_view, name = 'courses'),
    path("show_courses/<courses_id>", views.show_courses, name='show_courses')
]