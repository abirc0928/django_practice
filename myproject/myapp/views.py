from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def sayhello(request):
    return HttpResponse("hello, djngo")


def home(request):
    page = {"title": "Home page", "content": "Welcome to home page"}
    return render(request, "index.html", page)


def about(request):
    page = {"title": "About page", "content": "Welcome to About page"}
    return render(request, "about.html", page)


def contact(request):
    email = ("contact@exmple.com")
    title = ("Contact page")
    socialMedia = [
        "facebook: facebook.com",
        "twiter: twiter.com",
        "youtube: youtube.com",
        "instragram: instragram.com",
    ]
    hq = "x"
    return render(
        request,
        "contact.html",
        {"emailaddress": email, "socialMedia": socialMedia, "hq": hq, "title": title},
    )


def expriment(request, person = None):
    if person is None:
        person = "Guest"
    page = {"title": "Expriment page", "content": "Welcome to Expriment page",
            "data": person }
    return render(request, "expriment.html",page)
