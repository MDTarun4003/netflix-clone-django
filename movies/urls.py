from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('movie/<uuid:id>/', views.movie_detail, name='movie_detail'),
    path('genre/<int:genre_id>/', views.genre_movies, name='genre_movies'),
    path('search/', views.search, name='search'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('watchlist/add/<uuid:movie_id>/', views.add_to_watchlist, name='add_watchlist'),
    path('watchlist/remove/<uuid:movie_id>/', views.remove_from_watchlist, name='remove_watchlist'),
]