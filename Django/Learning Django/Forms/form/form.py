from django import forms
from django.core import validators

# METHOD 3 custom validator from validators
def check_for_bot(botcatcher_data):
    if len(botcatcher_data)>0:
        raise forms.ValidationError(('Invalid value'), code='invalid')

class FormElements(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)

    # METHOD 3 continued
    botcatcher = forms.CharField(widget=forms.HiddenInput, required=False,
                                    validators=[check_for_bot])    
    # METHOD 1 INBUILT VALIDATORS
    # botcatcher = forms.CharField(widget=forms.HiddenInput, required=False,
                                    # validators=[validators.MaxLengthValidator(0)])

    # METHOD 4 VALIDATE WHOLE FORM AT ONCE
    def clean(self):
        # name of method is a keyword for django to clean whole form.
        all_form_data = super().clean() # you will get dictionary of all data
        email = all_form_data['email']
        verify_email = all_form_data["verify_email"]
        print("Cleaning ")
        if email != verify_email:
            print("Invalid ")
            raise forms.ValidationError("Invalid Email")
    
    # METHOD 2 CUSTOM VALIDATORS
    # botcatcher = forms.CharField(widget=forms.HiddenInput, required=False,)

    # def clean_botcatcher(self):
    #     # This method is automatically called by django on forms.Form 
    #     # And the name of method should be "clean_<fieldname>()" where the field name is the 
    #     # name of the field to be verified. For example "clean_botcatcher" to validate
    #     # botcatcher. 
    #     # https://docs.djangoproject.com/en/3.0/ref/forms/validation/

    #     # print(self.cleaned_data)
    #     written_by_bot = self.cleaned_data['botcatcher']  # self.cleaned_data is a dictionary
    #     if len(self.written_by_bot)>0:
    #         raise forms.ValidationError("So You are a bot oki")
    #     return written_by_bot  
    #     # This return value will change the data stored in botcatcher.
    #     # for eg. return "Jumba" then the data stored in botcatcher will be "Jumba" not the data given by the bot.

