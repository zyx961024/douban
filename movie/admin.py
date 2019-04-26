from django.contrib import admin
from .models import Movie
# Register your models here.
# admin.site.register(Movie)
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','pic','name','director','star','comment')
    #倒序写-id
    ordering = ('id',)