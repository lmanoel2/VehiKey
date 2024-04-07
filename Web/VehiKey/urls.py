from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Camera/', include('Camera.urls')),
    path('Vehicle/', include('Vehicle.urls')),
]
