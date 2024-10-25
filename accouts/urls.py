from django.urls import path
from . import views
from .views import CustomPasswordResetView


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('reset_password/', CustomPasswordResetView.as_view(), name='password_reset'),
]
