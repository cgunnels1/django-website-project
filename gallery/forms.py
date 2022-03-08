# forms.py
from django import forms
from .models import *

class GalleryForm(forms.ModelForm):

	class Meta:
		model = Gallery
		fields = ['title', 'artist', 'image']
