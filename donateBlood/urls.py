from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainView.urls')),
    path("user/",include('user.urls')),
]
