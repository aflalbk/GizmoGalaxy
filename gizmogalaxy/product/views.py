from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, "index.html")

# to view the product list
def product_list(request):

    # take page number from user to view the page
    page_number = request.GET.get('page', 1)

    product_list = Product.objects.all()
    product_paginator = Paginator(product_list,1)
    page_list_obj = product_paginator.get_page(page_number)
    return render(request, "product_list.html", {"products" : page_list_obj, 'range_5': range(5)})

# to view the products details
def product_details(request):
    return render(request, "product_details.html")