from django.urls import path, include
from profileapi import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello_viewset')
"""Note: base_name is use to retrive the URL in our router """
router.register('profile', views.UserProfileViewSet)
"""Note: We dont need to give basename here because UserProfileViewSet has a queryset
that takes a name from models."""

urlpatterns = [
path('hello-view/', views.HelloApiVIew.as_view()),
path('', include(router.urls))
]
