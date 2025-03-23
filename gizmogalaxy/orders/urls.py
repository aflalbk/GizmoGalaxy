from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order, name="order"),
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
    path('remove_item/<int:pk>', views.remove_item, name="remove_item"),
    path('proceed_to_buy', views.proceed_to_buy, name="proceed_to_buy")
]