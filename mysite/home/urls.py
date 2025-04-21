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

    #acctal course 
    path("show_courses/<courses_id>", views.show_courses, name='show_courses'),
    path("lesson/<int:product_id>", views.lesson_view, name='lesson'),
    path("page/<page_id>", views.page, name='page'),
    path("quiz/<quiz_id>", views.quiz_view, name='quiz'),
    path("test/<test_id>", views.test_view, name='test'),


    #Categories Urls
    path('category/<str:cat>', views.category, name='category'),


    #My Courses Url
    path('my_courses', views.my_courses, name="my_courses" ),
    path('add', views.my_add, name="my_add" ),
    path('delete', views.my_delete, name="my_delete" ),
    path('update', views.my_update, name="my_update" ),

    #profile/user 
    path('profile_course_listings', views.profile_courses, name="profile_courses"),
    path('profile', views.profile, name="profile"),
]