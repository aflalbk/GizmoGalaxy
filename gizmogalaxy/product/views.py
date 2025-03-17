from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

# to view the product list
def product_list(request):
    return render(request, "product_list.html")

# to view the products details
def product_details(request):
    return render(request, "product_details.html")