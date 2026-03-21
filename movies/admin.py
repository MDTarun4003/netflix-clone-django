from django.contrib import admin

# Register your models here.
from .models import *

class MovieAdmin(admin.ModelAdmin):
  list_display = ('title', 'genre', 'release_date')
  search_fields = ('title',)
  list_filter = ('genre',)

admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)
admin.site.register(WatchList)