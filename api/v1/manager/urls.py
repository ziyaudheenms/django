from django.contrib import admin
from django.urls import path 
from . import views
urlpatterns = [
    path("" ,views.show),
    path("create/" ,views.create),
    path("delete/<int:pk>/" ,views.delete),
]
