from django.urls import path
from profileapi import views

urlpatterns = [
path('hello-view/', views.HelloApiVIew.as_view()),
]
