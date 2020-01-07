from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import User
from tracker.models import UserProfile

class RegistrationForm(forms.Form):
    email = forms.EmailField()
    number = PhoneNumberField()
    name = forms.CharField(max_length=256)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_email(self):
        email = self.cleaned_data["email"]
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists")
        return email

    def clean_password(self):
        password = self.cleaned_data["password"]
        # TODO: fix lazy/bad password strength test
        min_length = 7
        if len(password) < min_length:
            raise forms.ValidationError("Password must be at least {length}".format(length=min_length))
        return password

    def save(self):
        email = self.cleaned_data["email"]
        number = self.cleaned_data["number"]
        password = self.cleaned_data["password"]

        user = User.objects.create_user(username=email, email=email, password=password) 
        profile = UserProfile(user=user, number=number)
        profile.save()

        return profile
