from django.urls import path
from . import views

urlpatterns = [

    path('choose_plan/', views.choose_plan, name='choose_plan'),
    path('add_ons/', views.add_on_view, name='add_ons'),
    path('add_users/', views.user_profile_view, name='add_users'),
    path('payment/', views.payment, name='payment'),
    path('accept_payment/', views.accept_payment, name='accept_payment'),
    path('unsuccess_payment/', views.unsuccess_payment, name='unsuccess_payment'),
]

