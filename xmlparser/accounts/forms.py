from django import forms
from .models import User

class RegistrationForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Your First Name"}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Your Last Name"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control", "placeholder":"Your Email"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Your Password"}))
    password_confirm = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Your Password again"}))

    def clean(self):
        first_name = self.cleaned_data.get('first_name', None)
        last_name = self.cleaned_data.get('last_name', None)
        email = self.cleaned_data.get('email', None)
        password = self.cleaned_data.get('password', None)
        password_confirm = self.cleaned_data.get('password_confirm', None)
        if password and password_confirm:
            if password != password_confirm:
                msg = forms.ValidationError("Passwords do not match!")
                self.add_error("password", msg)
                self.add_error("password_confirm", msg)
        if email:
            user = User.objects.filter(email=email.strip())
            if user.exists():
                msg = forms.ValidationError("Email is already taken.")
                self.add_error("email", msg)

        return self.cleaned_data