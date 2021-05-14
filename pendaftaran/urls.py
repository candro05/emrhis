from django.contrib import admin
from django.urls import path, re_path
from Pendaftaran import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]

