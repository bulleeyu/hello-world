from django import forms
from django.core.files.base import ContentFile
from slugify import slugify
from urllib import request
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title','url','description')
    def clean(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg','jpeg','png']
