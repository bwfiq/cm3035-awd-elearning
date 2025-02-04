from django.urls import path
from users import views

urlpatterns = [
    path('', views.home, name='home'),
    path("users/<name>", views.hello_there, name='hello_there'),
]