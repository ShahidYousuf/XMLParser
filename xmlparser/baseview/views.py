from datetime import datetime
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from lxml import etree
from accounts.models import User, Student

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
            context = {
                'message': "Your data has been successfully uploaded."
            }
            return render(request, self.template_name, context)
        else:
            context = {
                'form': self.form_class(request.POST, request.FILES)
            }
            return render(request, self.template_name, context)

    def process_xml_upload(self, xmlfile=None, *args, **kwargs):
        if xmlfile is not None:
            xmltree = etree.parse(xmlfile)
            root = xmltree.getroot()
            for element in root.iter():
                if str(element.tag).strip().lower() == "student":
                    first_name = element.findtext("first_name", "")
                    last_name = element.findtext("last_name", "")
                    email = element.findtext("email", "")
                    dob = element.findtext("dob", None)
                    phone = element.findtext("phone", "")
                    gender = element.findtext("gender", "Male")
                    regd_number = element.findtext("registration_number", "")
                    total_marks = element.findtext("total_marks", 1000)
                    marks_obtained = element.findtext("marks_obtained", 0)
                    passed = element.findtext("passed", "1")
                    address = element.find("address")
                    city = state = country = zipcode = None
                    if address is not None:
                        city = address.findtext("city", "")
                        state = address.findtext("state", "")
                        country = address.findtext("country", "")
                        zipcode = address.findtext("zipcode", "")
                    std_user, is_present = User.objects.get_or_create(email=email)
                    std_user.username = email
                    std_user.first_name = first_name
                    std_user.last_name = last_name
                    std_user.is_active = True
                    std_user.set_password(email)
                    std_user.save()
                    student = Student(user=std_user)
                    student.city = city
                    student.state = state
                    student.country = country
                    student.zip = zipcode
                    student.gender = "M" if gender == "Male" else "F"
                    if dob is not None:
                        student.dob = datetime.strptime(dob, "%d/%m/%Y").date()
                    student.phone = phone
                    student.registration_numner = regd_number
                    student.total_marks = total_marks
                    student.marks_obtained = marks_obtained
                    if int(passed) == 1:
                        student.is_passed = True
                    else:
                        student.is_passed = False
                    student.save()

class UploadDetailView(LoginRequiredMixin, View):
    template_name = "baseview/details.html"
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    def get(self, request, *args, **kwargs):
        students = Student.objects.all().exclude(registration_numner__in = ["", " "])
        context = {
            "students": students
        }
        return render(request, self.template_name, context)



