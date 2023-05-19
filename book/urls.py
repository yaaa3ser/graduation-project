from django.urls import path
from .views import add_to_cart, view_cart, book_list, remove_from_cart

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('cart/', view_cart, name='view_cart'),
    path('cart/add/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:book_id>/', remove_from_cart, name='remove_from_cart'),
]