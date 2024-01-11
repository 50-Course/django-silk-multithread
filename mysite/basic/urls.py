from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("second/", views.index_2, name="index_2"),
]