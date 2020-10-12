from django import forms

class UploadFileForm(forms.Form):
    course = forms.CharField(max_length=50)
    FileName = forms.CharField(max_length=50)
    file = forms.FileField()