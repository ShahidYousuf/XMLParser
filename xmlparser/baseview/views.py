import xml
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UploadXMLForm

class HomePage(View):
    template_name = "baseview/home.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message" : "Welcome to Home Page"
        }
        return render(request, self.template_name, context)

class UploadView(View):
    template_name = "baseview/upload.html"
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    form_class = UploadXMLForm

    def get(self, request, *args, **kwargs):
        context = {
            'form': self.form_class()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        xmlfilelist = request.FILES.getlist('xmlfile', None)
        xmlfile = None
        if xmlfilelist is not None:
            xmlfile = xmlfilelist[0]
        if self.form_class(request.POST, request.FILES).is_valid():
            # now process the xml input
            self.process_xml_upload(xmlfile=xmlfile)
        else:
            context = {
                'form': self.form_class(request.POST, request.FILES)
            }
            return render(request, self.template_name, context)
        return redirect(to="home")

    def process_xml_upload(self, xmlfile=None, *args, **kwargs):
        if xmlfile is not None:
            pass

