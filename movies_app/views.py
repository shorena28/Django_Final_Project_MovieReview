from django.shortcuts import render


from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm


def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies_app/movie_form.html', {'form': form})


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies_app/movie_list.html', {'movies': movies})


def update_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies_app/movie_form.html', {'form': form})


def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movies_app/movie_confirm_delete.html', {'movie': movie})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies_app/movie_detail.html', {'movie': movie})

from .forms import ReviewForm
from .models import Review

def add_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.reviewer = request.user
            review.save()
            return redirect('movie_detail', pk=movie_id)
    else:
        form = ReviewForm()
    return render(request, 'movies_app/review_form.html', {'form': form, 'movie': movie})

from .models import Genre, Watchlist

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'movies_app/genre_list.html', {'genres': genres})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'movies_app/review_list.html', {'reviews': reviews})

def watchlist_list(request):
    watchlists = Watchlist.objects.all()
    return render(request, 'movies_app/watchlist_list.html', {'watchlists': watchlists})