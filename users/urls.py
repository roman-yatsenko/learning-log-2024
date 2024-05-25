from django.urls import include, path

from . import views

app_name = 'users'
urlpatterns = [
    # Додати URL авторизації за замовчуванням
    path('', include('django.contrib.auth.urls')),
    # Сторінка реєстрації
    path('register/', views.register, name='register'),
]
