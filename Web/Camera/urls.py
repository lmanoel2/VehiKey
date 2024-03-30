from . import views

from django.urls import path

urlpatterns = [
    path('', views.camera, name='camera')
]