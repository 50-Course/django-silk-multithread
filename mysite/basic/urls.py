from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("slow/", views.slow_index, name="slow_index"),
]