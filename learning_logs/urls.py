"""Визначає схеми URL для learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Домашня сторінка
    path('', views.index, name='index'),
    # Сторінка з переліком всіх тем
    path('topics/', views.topics, name='topics'),
]
