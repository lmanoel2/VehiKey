from . import views

from django.urls import path

urlpatterns = [
    path('', views.vehicle, name='vehicle'),
]