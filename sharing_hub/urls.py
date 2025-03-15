from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("upload", views.upload, name="upload"),
    path("dashboard", views.dashboard, name="dashboard"),
]
