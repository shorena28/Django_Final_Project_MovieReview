"""
URL configuration for MovieReviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from movies_app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.movie_list, name='movie_list'),
    path('create/', views.create_movie, name='create_movie'),
    path('update/<int:pk>/', views.update_movie, name='update_movie'),
    path('delete/<int:pk>/', views.delete_movie, name='delete_movie'),
    path('genres/', views.genre_list, name='genre_list'),
    path('reviews/', views.review_list, name='review_list'),
    path('watchlists/', views.watchlist_list, name='watchlist_list'),
]