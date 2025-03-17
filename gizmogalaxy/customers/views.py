from django.shortcuts import render

# Create your views here.
def log_in_or_register(request):
    return render(request, "log_in_or_register.html")