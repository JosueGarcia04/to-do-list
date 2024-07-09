from django.urls import path
from . import views
#global
urlpatterns =[
    path("", views.index, name="index" ), 
    path("insert/", views.insert, name="insert"),
]