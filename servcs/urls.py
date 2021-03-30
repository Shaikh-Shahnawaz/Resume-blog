from servcs import views
from django.urls import path

urlpatterns = [
  
    path('services/', views.services, name='servicesName' ),
]
