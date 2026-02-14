from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib import messages


def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            next_page = request.POST.get("next") or request.GET.get("next")
            if not next_page or next_page == "login":
                next_page = "invApp:home"
            return redirect(next_page)
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect("invApp:home")
    error_message = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_page = request.POST.get("next") or request.GET.get("next") or "invApp:home"
            if not next_page or next_page == "login":
                next_page = "invApp:home"
            return redirect(next_page)
        else:
            error_message = "Invalid username or password."
    return render(
        request,
        "login.html",
        {"error": error_message, "next": request.GET.get("next", "")},
    )


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("authApp:login")
    return redirect("productlist")


@login_required
def Home_view(request):
    return render(request, "auth_app/home.html")


class ProtectedView(LoginRequiredMixin, View):
    login_url = "authApp:login"
    redirect_field_name = "next"

    def get(self, request):
        return render(request, "registration/protected.html")
