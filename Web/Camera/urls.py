from . import views

from django.urls import path

urlpatterns = [
    path('', views.camera, name='camera'),
    path('update_camera/', views.update_camera, name='update_camera')
]