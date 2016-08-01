from django.db.models import Q
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from movie.models import Movie


class MovieView(View):

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        movies_qs = Movie.objects.all()
        if search:
            query = Q(name__icontains=search) | Q(theater__name__icontains=search)
            movies_qs = movies_qs.filter(query)
        paginator = Paginator(movies_qs, 10)
        page = request.GET.get('page')
        try:
            movies = paginator.page(page)
        except PageNotAnInteger:
            movies = paginator.page(1)
        except EmptyPage:
            movies = paginator.page(paginator.num_pages)
        return render(request, 'movies.html', {'movies': movies})
