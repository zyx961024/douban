from django.urls import path
from .import views
urlpatterns = [
    #localhost:8080:movie/
    #start with:movie/
    path('<int:movie_id>', views.movie_detail,name='movie_detail'),
    path('', views.movie_list,name='movie_list'),
]
