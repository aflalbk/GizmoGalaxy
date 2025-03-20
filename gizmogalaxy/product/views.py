from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    top_4_products = Product.objects.order_by("-rating")[:3]
    top_priorty_products = Product.objects.order_by("-priority")[:4]
    latest_products = Product.objects.order_by("-created_on")[:8]
    return render(request, "index.html", {'top_4_products': top_4_products, 'top_priorty_products':top_priorty_products, 'latest_products':latest_products})

# to view the product list
def product_list(request):

    # take page number from user to view the page
    page_number = request.GET.get('page', 1)

    product_list = Product.objects.order_by("-priority")
    product_paginator = Paginator(product_list,4)
    page_list_obj = product_paginator.get_page(page_number)
    return render(request, "product_list.html", {"products" : page_list_obj, 'range_5': range(5)})

# to view the products details
def product_details(request, pk): # 
    product = Product.objects.get(pk=pk)
    top_4_products = Product.objects.order_by("-rating")[:4]

    return render(request, "product_details.html", {"product": product, "top_4_products":top_4_products, 'range_5': range(5)})