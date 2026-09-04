from django.shortcuts import render
from .models import Movie
# # Create your views here.
# movies = [
#     {
#         'id': 1,
#         'name': 'the 67dessy',
#         'price': 67,
#         'description': "the trojan horse failed and Troy lived"
#     },
#     {
#         'id': 2,
#         'name': 'the 67dessy 2',
#         'price': 3,
#         'description': "odyssus stayed in that place with white lotus"
#     },
#     {
#         'id': 3,
#         'name': 'buzz infinity',
#         'price': 4,
#         'description': "gt buzz goes infinity and behind"
#     },
#     {
#         'id': 4,
#         'name': 'spiderman no way home',
#         'price': 5,
#         'description': "no way spiderman"
#     },
# ]

def index(req):
    search_term = req.GET.get('search')
    if search_term:
        movies = Movie.objects.filter(name__icontains=search_term)
    else:
        movies = Movie.objects.all()

    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = movies
    return render(req, 'movies/index.html', {'template_data': template_data})

def show(req, id):
    movie = Movie.objects.get(id=id)

    template_data = {}
    template_data['title'] = movie.name
    template_data['movie'] = movie
    return render(req, 'movies/show.html', {'template_data': template_data})