from django.urls import path
from . import views

urlpatterns = [
    path('choose_plan/', views.plan_view, name='plan_view'),
    path('add_ons/', views.add_ons, name='add_ons'),
    path('add_ons/add_users/', views.add_users, name='add_users'),
    path('payment/', views.payment, name='payment'),
    path('accept_payment/', views.accept_payment, name='accept_payment'),
    path('unsuccess_payment/', views.unsuccess_payment, name='unsuccess_payment'),
]

