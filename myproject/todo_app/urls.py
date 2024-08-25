from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_lsit),
    path('<int:pk>/', views.task_details, name='task_details'),
]

