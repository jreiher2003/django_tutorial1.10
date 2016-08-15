from django import forms 
from .models import SignUp 

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp 
        fields = ["email", "full_name"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        email_username, e_provider = email.split("@")
        school, extention = e_provider.split(".")
        if not extention == "edu":
            raise forms.ValidationError("Please use a valid .edu address")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data["full_name"]
        #validation code goes here
        return full_name