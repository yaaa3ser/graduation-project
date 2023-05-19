from django.shortcuts import render, redirect
from .models import Book, Cart
from django.http import JsonResponse
from .dummy_data import DUMMY_BOOKS


def book_list(request):
    if len(Book.objects.all()) < 40:
        for book in DUMMY_BOOKS:
            Book.objects.get_or_create(**book)
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def add_to_cart(request, book_id):
    book = Book.objects.get(pk=book_id)

    # Get the user's cart or create a new cart if it doesn't exist
    cart, _ = Cart.objects.get_or_create()

    # Add the book to the cart
    cart.books.add(book)

    
    # Redirect back to the book listing or any other desired page
    return redirect('book_list')


def view_cart(request):
    # Get the user's cart or create a new cart if it doesn't exist
    cart, _ = Cart.objects.get_or_create()

    # Retrieve the books in the cart
    books = cart.books.all()

    # Pass the cart to the template
    return render(request, 'cart.html', {'books': books})


def remove_from_cart(request, book_id):
    # Get the user's cart or create a new cart if it doesn't exist
    cart, _ = Cart.objects.get_or_create()

    # Remove the book from the cart
    cart.books.remove(book_id)

    return redirect('view_cart')
