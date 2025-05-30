from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainView, name='home'),
    path('search_donors/', views.search_donors, name='search_donors'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]