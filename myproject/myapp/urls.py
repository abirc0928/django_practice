from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.sayhello),
    path("", views.home),
    path("home/", views.home),
    path("about/", views.about),
    path("contact/", views.contact),
    path("expriment/", views.expriment),
    path("expriment/<person>", views.expriment),
]
