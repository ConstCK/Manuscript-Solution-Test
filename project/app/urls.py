from django.contrib import admin
from django.urls import path, include

from .views import file_to_db, db_to_file


urlpatterns = [
    path('create_db/', file_to_db),
    path('create_file/', db_to_file)
]