from django import forms
from mainapp.misc_resources import resources as var

# we will not apply drop down in for cities as total cities are 20820 which takes time and gives bad experiance instead we will just give text area for city.

# initial parameter is used to provide initial default value
# choices are the dropdown select options
# ChoiceField are used to create dropdown menu
class UserParam(forms.Form):
    '''
    Front-end setup
    '''
    R = var.resources()
    city_name = forms.CharField(label='City Name')
    units = forms.ChoiceField(label='Unit', 
                                choices=R.unit_choice,
                                initial='celsius')
    language = forms.ChoiceField(label='Language', 
                                choices=R.lang_choice,
                                initial='en')
    tz = forms.ChoiceField(label='Time Zone',
                            choices=R.timezone,
                            initial='IST')