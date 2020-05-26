from django import forms

class FileUpload(forms.Form):
    audio_File = forms.FileField()