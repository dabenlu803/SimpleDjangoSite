__author__ = 'lilu'
from django import forms


class PersonalInfoItem(forms.Form):
    name = forms.CharField(max_length=20)
    phoneNum = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=100, required=True)
    location = forms.CharField(max_length=100)
    job = forms.CharField(max_length=50)
    company = forms.CharField(max_length=50)
