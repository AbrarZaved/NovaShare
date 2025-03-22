from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("upload", views.upload, name="upload"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("delete_item/<str:slug>", views.delete_item, name="delete_item"),
    #path("share/<str:slugs>", views.UploadView.as_view(), name="share"),
    path("share/<str:slugs>", views.shared_page, name="share"),
]
