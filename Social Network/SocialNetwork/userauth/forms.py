from django import forms
from django.contrib.auth.models import User


class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.widgets.PasswordInput())

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.widgets.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.widgets.PasswordInput, label = 'Repeat Password')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1']!=cd['password2']:
            raise forms.ValidationError('Password didn\'t match')
        return cd['password2']