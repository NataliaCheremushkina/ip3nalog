from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('send_feedback/', views.send_feedback, name='send_feedback'),
]
