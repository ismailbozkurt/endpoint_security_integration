from django.shortcuts import render
from utils.products import get_products
# from django.views.decorators.csrf import csrf_exempt


def index(request):
    products = get_products()
    return render(
        request,
        'index.html',
        {
            "data": products,
        })
