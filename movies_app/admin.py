from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Movie, Genre, Review, Watchlist

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Watchlist)