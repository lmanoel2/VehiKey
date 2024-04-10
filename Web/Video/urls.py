from . import views

from django.urls import path

urlpatterns = [
    path('', views.video, name='video'),
    path('stream/', views.stream, name='stream'),
    path('keep-alive/', views.keep_alive, name='keep_alive'),
    path('changed-cam/', views.changed_cam, name='changed_cam'),
]