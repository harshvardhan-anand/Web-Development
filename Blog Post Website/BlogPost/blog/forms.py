from django import forms
from .models import Comments

class EmailForm(forms.Form):
    email = forms.EmailField(max_length=25)
    to = forms.EmailField(max_length=25)
    message = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'comment')
