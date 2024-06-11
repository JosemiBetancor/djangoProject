from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<int:id>', views.hello),
    path('projects/', views.project),
    path('tasks/<int:id>', views.Tasks),
    path('tasks/title/<str:title>', views.TasksperTitle),
    path('projectsh/', views.projecthtml),
    path('Taskh/', views.taskhtml)
]