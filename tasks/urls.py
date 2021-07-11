# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"), # 루트 url
    path('delete/<str:id>/', views.deleteTask, name="delete"),
    path('edit/<str:id>', views.edit, name="edit"),
    path('update/<str:id>', views.update, name="update"),


]
