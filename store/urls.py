from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),

    path(
        'cart/add/<int:book_id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/increase/<int:book_id>/',
        views.increase_quantity,
        name='increase_quantity'
    ),

    path(
        'cart/decrease/<int:book_id>/',
        views.decrease_quantity,
        name='decrease_quantity'
    ),

    path(
        'cart/remove/<int:book_id>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),

    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),

    path(
        'order-success/<int:order_id>/',
        views.order_success,
        name='order_success'
    ),
]