from django.contrib import admin
from django.urls import path, include

from .views import data_in, data_out, data_in_success, data_out_success, error_page

urlpatterns = [
    path('data_in/', data_in),
    path('data_out/', data_out),
    path('data_in_success/', data_in_success),
    path('data_out_success/', data_out_success),
    path('error_page/', error_page),
]
