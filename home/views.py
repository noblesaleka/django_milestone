from django.shortcuts import render
from products.models import Product, Category


def index(request):
    """ A view to return index page """
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, 'home/index.html', context)
