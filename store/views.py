from django.shortcuts import render, get_object_or_404
from .models import Book, Category


def book_list(request):
    books = Book.objects.all()
    categories = Category.objects.all()

    search_query = request.GET.get('search')
    category_id = request.GET.get('category')

    if search_query:
        books = books.filter(
            title__icontains=search_query
        ) | books.filter(
            author__icontains=search_query
        )

    if category_id:
        books = books.filter(category_id=category_id)

    return render(request, 'books/book_list.html', {
        'books': books,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_id,
    })


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    return render(request, 'books/book_detail.html', {
        'book': book,
    })