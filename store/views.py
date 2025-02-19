from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    return render(request, 'menu.html')

def cart(request):
    return render(request, 'cart.html')

def login(request):
    return render(request, 'login.html')

def checkout(request):
    return render(request, 'checkout.html')

def account(request):
    return render(request, 'account.html')