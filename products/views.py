from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
# from . import settings
from django.http import HttpResponse


def all_products(request):
    """ A view to show all products, including sorting and search queries"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def author_detail(request, author_id):
    """ A view to show individual author details """

    author = get_object_or_404(Product, pk=author_id)

    context = {
        'author': author,
    }

    return render(request, 'products/author_detail.html', context)


# def download(request,path):
#     file_path = os.path.join(settings.MEDIA_ROOT,path)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(),content_type="application/pdf")
#             response['Content-Disposition'] = 'inline;filename='+ os.path.basename(file_path)
#             return response

#     raise HttpResponse
