from django.contrib import admin
from .models import Movie, Review

# Register your models here.

# ordering movies by name
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name'] # allow search by name
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)