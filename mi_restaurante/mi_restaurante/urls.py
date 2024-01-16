# mi_restaurante/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('platillos/', include('platillos.urls')),
]
