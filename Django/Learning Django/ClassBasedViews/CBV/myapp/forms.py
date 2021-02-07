from django import forms

class BasicForm(forms.Form):
    name = forms.CharField(max_length=10)
    email = forms.EmailField(required=False)