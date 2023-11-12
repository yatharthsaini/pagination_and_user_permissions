from django.shortcuts import render
from .models import Movie


def movie_list(request):
    list_movies = Movie.objects.all()
    return render(request, 'movies/movie_html.html', {'list_movies': list_movies})
