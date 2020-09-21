from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm

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
            pass
        else:
            context = {
                "error": True,
                "message": "email and password are required",
                "next": next_url
            }
            return render(request, self.template_name, context)
        return redirect(to=next_url)