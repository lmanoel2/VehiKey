from . import views

from django.urls import path

urlpatterns = [
    path('', views.camera, name='camera'),
    path('get_camera/', views.get_camera, name='get_camera')
]