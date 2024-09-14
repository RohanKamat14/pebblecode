from django.contrib import admin
from django.urls import path, include
from .import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("home.urls")),
    path("courses/", include("courses.urls")),
    path("login/", include("home.urls")),
    path('admin/', admin.site.urls),
    path("Signup/", include("home.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
