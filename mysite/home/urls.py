from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name='login'),
    path("Signup", views.Signup, name = 'Signup'),
    path("logout", views.logout_view, name = 'logout'),
    path("courses", views.courses_view, name = 'courses')
]