from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Movie)

admin.site.register(models.Showtime)

admin.site.register(models.Theater)

admin.site.register(models.Tags)
