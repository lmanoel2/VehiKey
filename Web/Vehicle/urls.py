from . import views

from django.urls import path

urlpatterns = [
    path('', views.vehicle, name='vehicle'),
    path('get_vehicle/', views.get_vehicle, name='get_vehicle'),
    path('update_vehicle/', views.update_vehicle, name='update_vehicle'),
    path('delete_vehicle/', views.delete_vehicle, name='delete_vehicle'),
]