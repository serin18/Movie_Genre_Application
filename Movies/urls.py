"""Movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MOVIE.views import (
    genre_list, genre_detail, create_genre, update_genre,
    movie_list, movie_detail, create_movie, update_movie,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', genre_list, name='genre_list'),
    path('genres/<int:genre_id>/', genre_detail, name='genre_detail'),
    path('genres/create/', create_genre, name='create_genre'),
    path('genres/update/<int:genre_id>/', update_genre, name='update_genre'),

    path('movies/', movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('movies/create/', create_movie, name='create_movie'),
    path('movies/update/<int:movie_id>/', update_movie, name='update_movie'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)