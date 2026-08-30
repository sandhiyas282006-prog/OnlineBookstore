from django.shortcuts import render, get_object_or_404
from .models import Book


def book_list(request):
    books = Book.objects.all()

    search_query = request.GET.get('search')

    if search_query:
        books = books.filter(
            title__icontains=search_query
        ) | books.filter(
            author__icontains=search_query
        )

    return render(request, 'books/book_list.html', {
        'books': books,
        'search_query': search_query,
    })


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    return render(request, 'books/book_detail.html', {
        'book': book,
    })