from django import forms
from .models import *

class SongForm(forms.ModelForm):

	class Meta:
		model = Song
		fields = ['title', 'writer', 'audioFile']