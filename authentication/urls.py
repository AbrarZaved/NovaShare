from django.urls import path, include
from . import views

urlpatterns = [
    path("login", views.sign_in, name="login"),
    path("logout", views.sign_out, name="logout"),
    path("profile", views.profile, name="profile"),
]
