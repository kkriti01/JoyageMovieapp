from django.conf.urls import url
from django.contrib import admin

from movie import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.MovieView.as_view(), name='home'),
    url(r'^movies/', views.MovieView.as_view(), name='movies'),
]
