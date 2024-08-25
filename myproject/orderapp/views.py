from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def order(request):
    page = {"title": "Order page", "content": "Welcome to Order page"}

    return render(request, "order.html", page)
