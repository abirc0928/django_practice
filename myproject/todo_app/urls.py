from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_lsit, name="task_lsit"),
    path('<int:pk>/', views.task_details, name='task_details'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:pk>', views.delete_task, name='delete_task'),
    path('update/<int:pk>', views.update_task, name='update_task'),
    path('addForm/', views.add_task_form, name='addForm'),
    path('updateForm/<int:pk>', views.update_task_form, name='update_form'),
]

