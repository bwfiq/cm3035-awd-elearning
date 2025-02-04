from django.urls import path
from users import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path("users/<name>", views.hello_there, name='hello_there'),
]