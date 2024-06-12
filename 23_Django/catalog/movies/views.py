from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Movie
# Create your views here.

# http://127.0.0.1:8000

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/list.html', context=context)
    
def detail(request, movie_id):
    
    # try:
    #     movie = Movie.objects.get(pk = movie_id)
    # except Movie.DoesNotExist:
    #     raise Http404('This film does not exist!')
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context=context)
    
def search(request):
    return render(request, 'movies/search.html')
    