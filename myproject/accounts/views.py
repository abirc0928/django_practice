from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# need customize to visit abstracuser
# need more customize to visit abstracbaseuser
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username", "password", "first_name", "last_name"]


def registration(request):
    if request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("registration")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/registration.html", context)

def home(request):
    #read session
    user_email =  request.session.get('email')
    contex = {
        "user_email": user_email
    }
    return render(request, "accounts/home.html", contex )

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            #session set
            request.session['email'] = user.email
            login(request, user)
            return redirect("account_home")
    else:
        form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request, "accounts/login.html",context)

def logout_view(request):
    logout(request)
    return redirect("login")