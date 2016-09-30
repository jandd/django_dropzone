from django import forms

from django_dropzone.models import UploadFile


class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['image']
