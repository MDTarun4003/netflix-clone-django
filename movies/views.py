from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def home(request):
  movies = Movie.objects.all()
  genres = Genre.objects.all()
  return render(request, 'movies/home.html', {'movies': movies,'genres': genres})

@login_required
def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    recommended = Movie.objects.filter(genre=movie.genre).exclude(id=movie.id)[:5]
    return render(request, 'movies/detail.html', {'movie': movie,'recommended': recommended})

@login_required
def genre_movies(request, genre_id):
    movies = Movie.objects.filter(genre_id=genre_id)
    genres = Genre.objects.all()
    return render(request, 'movies/home.html', {'movies': movies,'genres': genres})

@login_required
def search(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(title__icontains=query)
    else:
        movies = []
    return render(request, 'movies/search.html', {'movies': movies,'query': query})

@login_required
def add_to_watchlist(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    WatchList.objects.get_or_create(user=request.user, movie=movie)
    return redirect('home')


@login_required
def remove_from_watchlist(request, movie_id):
    WatchList.objects.filter(user=request.user, movie_id=movie_id).delete()
    return redirect('watchlist')


@login_required
def watchlist(request):
    items = WatchList.objects.filter(user=request.user)
    return render(request, 'movies/watchlist.html', {'items': items})