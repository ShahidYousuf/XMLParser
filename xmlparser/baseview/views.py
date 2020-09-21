from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePage(View):
    template_name = "baseview/home.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message" : "Welcome to Home Page"
        }
        return render(request, self.template_name, context)
