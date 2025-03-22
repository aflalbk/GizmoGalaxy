from django.urls import path
from . import views

urlpatterns = [
    path('log_in_or_register/', views.log_in_or_register, name="log_in_or_register"),
    path('sign_out/', views.sign_out, name='sign_out')
]