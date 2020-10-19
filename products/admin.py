from django.contrib import admin
from .models import Product, Category, Author

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'title',
        'author',
        'description',
        'price',
        'sale_price',
        'category',
        'rating',
        'image',
        'download',
    )

    ordering = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
