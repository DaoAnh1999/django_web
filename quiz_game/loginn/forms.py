from django import forms
from django.core import validators

class Input(forms.Form):
    input = forms.IntegerField(initial=0)