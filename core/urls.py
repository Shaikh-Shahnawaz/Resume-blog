from core import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="homename"),
    path('contact/', views.contact, name="contactName"),
]
