from django import forms
from .utility.data import Data

class UserData(forms.Form):
    df = Data()
    for column in df.columns:
        if column not in ['nkill','nwoundte', 'nwound','nperps','nkillter', 'nperpcap','longitude','latitude']:
            # yahan globals() kaam ni karega as here we need local variable
            locals()[column] = forms.ChoiceField(choices=df.choices(column))