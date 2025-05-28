from django import forms
from .models import Movie, Review

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date', 'genres']

class ReviewForm(forms.ModelForm): 
    class Meta:
        model = Review
        fields = ['rating', 'comment']