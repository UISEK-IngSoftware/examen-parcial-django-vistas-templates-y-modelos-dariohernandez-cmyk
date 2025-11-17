from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'publication_year', 'director_name', 'genre', 'synopsis', 'image']
