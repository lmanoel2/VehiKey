from . import views

from django.urls import path

urlpatterns = [
    path('', views.control, name='control'),
    path('send_command/', views.send_command, name='send_command'),
]
