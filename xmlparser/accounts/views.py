from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from .models import User

class LoginView(View):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm

    def get(self, request, *args, **kwargs):
        next_url = request.GET.get("next", "/")
        context = {
            "message" : "Welcome to Login Page",
            "form": self.form_class(),
            "next_url": next_url
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        post_data = request.POST.copy()
        next_url = post_data.get('next', '/')
        email = post_data.get('email', None)
        password = post_data.get('password', None)
        if email and password:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(to=next_url)
            else:
                context = {
                    "error" : True,
                    "message": "Invalid email or password",
                    "next_url": next_url
                }
                return render(request, self.template_name, context)
        else:
            context = {
                "error": True,
                "message": "email and password are required",
                "next_url": next_url
            }
            return render(request, self.template_name, context)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(to="/")


class RegisterView(View):
    template_name = "accounts/register.html"
    form_class = RegistrationForm

    def get(self, request, *args, **kwargs):
        context = {
            "form": self.form_class()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        register_form = self.form_class(request.POST.copy())
        if register_form.is_valid():
            first_name = register_form.cleaned_data.get("first_name", "")
            last_name = register_form.cleaned_data.get("last_name", "")
            email = register_form.cleaned_data.get("email", "")
            password = register_form.cleaned_data.get("passoword", "")
            user = User.objects.create(email=email)
            user.username = email
            user.first_name = first_name
            user.last_name = last_name
            user.set_password(password)
            user.is_active = True
            user.is_staff = True
            user.is_superuser = False
            user.save()
            return redirect(to="/")
        else:
            context = {
                "message": "Account creation failed! Please correct the following errors.",
                "form": self.form_class(request.POST.copy()),
            }
            return render(request, self.template_name, context)