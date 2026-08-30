from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Cart, Order, OrderItem


def get_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


def add_to_cart(request, book_id):
    session_key = get_session_key(request)
    book = get_object_or_404(Book, id=book_id)

    cart_item, created = Cart.objects.get_or_create(
        session_key=session_key,
        book=book,
        defaults={'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


def cart_view(request):
    session_key = get_session_key(request)

    cart_items = Cart.objects.filter(session_key=session_key)

    total = sum(item.total_price() for item in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })


def increase_quantity(request, book_id):
    session_key = get_session_key(request)

    cart_item = get_object_or_404(
        Cart,
        session_key=session_key,
        book_id=book_id
    )

    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')


def decrease_quantity(request, book_id):
    session_key = get_session_key(request)

    cart_item = get_object_or_404(
        Cart,
        session_key=session_key,
        book_id=book_id
    )

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')


def remove_from_cart(request, book_id):
    session_key = get_session_key(request)

    cart_item = get_object_or_404(
        Cart,
        session_key=session_key,
        book_id=book_id
    )

    cart_item.delete()

    return redirect('cart')

def checkout(request):
    session_key = get_session_key(request)

    cart_items = Cart.objects.filter(session_key=session_key)

    if not cart_items.exists():
        return redirect('cart')

    total = sum(item.total_price() for item in cart_items)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        order = Order.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            total_amount=total
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                book=item.book,
                quantity=item.quantity,
                price=item.book.price
            )

        cart_items.delete()

        return redirect('order_success', order_id=order.id)

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total': total
    })

def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    return render(request, 'order_success.html', {
        'order': order
    })

def home(request):
    return render(request, 'home.html')

def home(request):
    books = Book.objects.all()

    return render(request, 'home.html', {
        'books': books
    })