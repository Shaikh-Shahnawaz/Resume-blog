from eductn import views
from django.urls import path, include

urlpatterns = [
  
    path('skill/', views.skill, name='skillName'),
]