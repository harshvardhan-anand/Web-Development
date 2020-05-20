from django import forms
from form.models import UserProfile

class UserForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = "__all__"
