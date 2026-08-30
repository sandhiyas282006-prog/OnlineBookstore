from django.contrib import admin
from .models import Category, Book, Subscriber, Cart, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'category',
        'price',
        'is_best_seller',
        'is_new_arrival',
    )
    search_fields = ('title', 'author')


admin.site.register(Subscriber)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)