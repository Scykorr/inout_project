from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('reset_password/', views.reset_password_view, name='reset_password'),
]
