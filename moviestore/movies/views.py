from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review
from django.contrib.auth.decorators import login_required
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
    reviews = Review.objects.filter(movie=movie)

    template_data = {}
    template_data['title'] = movie.name
    template_data['movie'] = movie
    template_data['reviews'] = reviews
    return render(req, 'movies/show.html', {'template_data': template_data})

@login_required
def create_review(req, id):
    if req.method == 'POST' and req.POST['comment'] != '':
        movie = Movie.objects.get(id=id)
        review = Review()
        review.comment = req.POST['comment']
        review.movie = movie
        review.user = req.user
        review.save()
        return redirect('movies.show', id=id)
    else:
        return redirect('movies.show', id=id)


@login_required
def edit_review(req, id, review_id):
    review = get_object_or_404(Review, id=review_id)
    if req.user != review.user:
        return redirect('movies.show', id=id)

    if req.method == 'GET':
        template_data = {}
        template_data['title'] = 'Edit Review'
        template_data['review'] = review
        return render(req, 'movies/edit_review.html', {'template_data': template_data})
    elif req.method == 'POST' and req.POST['comment'] != '':
        review = Review.objects.get(id=review_id)
        review.comment = req.POST['comment']
        review.save()
        return redirect('movies.show', id=id)
    else:
        return redirect('movies.show', id=id)

@login_required
def delete_review(req, id, review_id):
    review = get_object_or_404(Review, id=review_id, user=req.user)
    review.delete()
    return redirect('movies.show', id=id)