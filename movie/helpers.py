import requests
from dateutil.parser import parse

from movie import models


def feth_movies_data(url='http://188.166.208.228/us_movies/'):
    response = requests.get(url)
    theatre_list = response.json()
    for theatre in theatre_list:
        movie_list = theatre['movies']
        theater_link = theatre['theater_link']
        theater_name = theatre['theater_name']
        city = theatre['city']
        address = theatre['address']
        print(theater_name)
        theater_obj, created = models.Theater.objects.get_or_create(name=theater_name)
        if created:
            theater_obj.link = theater_link
            theater_obj.name = theater_name
            theater_obj.city = city
            theater_obj.address = address
            theater_obj.save()
        for movie in movie_list:
            name = movie['name']
            tags = movie['tags']
            image = movie['image']
            timings_link = movie['timings_link']
            screen_format = movie['screen_format']
            duration = movie['duration']
            print(name)
            movie_obj, created = models.Movie.objects.get_or_create(name=name, theater=theater_obj)
            if created:
                movie_obj.image = image
                movie_obj.screen_format = screen_format,
                movie_obj.duration = duration
                movie_obj.save()
            for tag in tags:
                tag, created = models.Tags.objects.get_or_create(name=tag)
                tag.movie.add(movie_obj)

            for timings in timings_link:
                book_link = timings['book_link']
                time = parse(timings['time']).time()
                show_time, created = models.Showtime.objects.get_or_create(movie=movie_obj, time=time)
                if created:
                    show_time.book_link = book_link or ''
                    show_time.save()
