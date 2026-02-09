from django.urls import path
from movies.api import views 

urlpatterns = [
    path("", views.movie_list, name="movie-list"),
    path("create/", views.movie_create, name="movie-create"),
    path("<int:pk>/", views.movie_detail, name="movie-detail"),
    path("<int:pk>/edit/", views.movie_edit, name="movie-edit"),
    path("<int:pk>/delete/", views.movie_delete, name="movie-delete"),
]