from __future__ import unicode_literals
from django import forms
from .models import Photo
from django.contrib.auth.models import User

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('filtered_image',)
        fields = ('image', 'content', )



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']