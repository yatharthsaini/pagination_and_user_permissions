from django.urls import path
from .views import movie_list

urlpatterns = [
    path('movie-list/', movie_list, name='movie-list')
]