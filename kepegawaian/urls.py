from django.contrib import admin
from django.urls import path

from . import views

app_name = 'kepegawaian'

urlpatterns = [
    path('data/pegawai/', views.data_pegawai, name='data_pegawai'),
    path('data/pegawai/add/', views.add_data_pegawai, name='add_data_pegawai'),
    path('data/pegawai/edit/<int:id>/', views.edit_data_pegawai, name='edit_data_pegawai'),
    path('data/pegawai/delete/<int:id>/', views.delete_data_pegawai, name='delete_data_pegawai'),
]
