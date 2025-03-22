from django.shortcuts import render, redirect
from . models import Customer
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def log_in_or_register(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register'] = True # For login and register tabs to show correctly
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            address = request.POST.get("address")
            phone = request.POST.get("phone")
        
            # Create Customer account
            Customer.objects.create(
                username = username,
                email = email,
                password = password,
                address = address,
                phone = phone
            )
            registration_success = "Successfully Registered"
            messages.success(request, registration_success)
            context['register'] = False
            
        except Exception as e :
            error_message = "Duplicate user name or invalid input data"
            messages.error(request, error_message)

    

    if request.POST and 'log_in' in request.POST:
        context["register"]=False # For login and register tabs to show correctly

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        print(user)
        print(user.is_authenticated)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "invalid user credentials")

    
    return render(request, "log_in_or_register.html", context)

def sign_out(request):
    logout(request)
    return redirect('index')