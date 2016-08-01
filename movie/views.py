from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from movie.models import Movie


class MovieView(View):

    def get(self, request, *args, **kwargs):
        movies_qs = Movie.objects.all()
        paginator = Paginator(movies_qs, 10)
        page = request.GET.get('page')
        try:
            movies = paginator.page(page)
        except PageNotAnInteger:
            movies = paginator.page(1)
        except EmptyPage:
            movies = paginator.page(paginator.num_pages)
        return render(request, 'movies.html', {'movies': movies})
