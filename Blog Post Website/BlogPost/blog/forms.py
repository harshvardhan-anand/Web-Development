from django import forms
from .models import Comments

class EmailForm(forms.Form):
    email = forms.EmailField(max_length=25)
    to = forms.EmailField(max_length=25)
    message = forms.CharField(required=False, widget=forms.Textarea)

    email.widget.attrs.update({
        'class':'form-control'
    })
    to.widget.attrs.update({
        'class':'form-control'
    })
    message.widget.attrs.update({
        'class':'form-control',
        'rows':3,
    })

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'comment')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # https://docs.djangoproject.com/en/3.1/ref/forms/widgets/#styling-widget-instances
    # adding bootstrap classes to "input area (those boxes like:textarea box)" of html
        self.fields['name'].widget.attrs.update({
            'class':'form-control',
        })

        self.fields['comment'].widget.attrs.update({
            'class':'form-control',
            'rows':3,
        })
