# yaha par ham import karenge logic jo views me likha hai
from django.urls import path  # path ek function hai jo URLs ka mapping karta hai.
from . import views # Yahan . ka matlab hota hai "current directory". views file ko import kar raha hai jo tumhare current folder ke andar hoti hai.

urlpatterns = [
    path('', views.home, name="home"),
    path('api/get-quiz/', views.get_quiz, name="get_quiz"),
    path('quiz/', views.quiz, name='quiz')
]