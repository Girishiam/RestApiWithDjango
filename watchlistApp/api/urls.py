
from django.urls import path,include
from watchlistApp.api.views import MovieList,MovieDetails
# from watchlistApp.api.views import movies,movie_details
urlpatterns = [
    # path('list/',movies,name='movie_list'),
    # path('list/<int:pk>/',movie_details,name='movie_details'),
    path('list/', MovieList.as_view(),name='movie_list'),
    path('list/<int:pk>/', MovieDetails.as_view(),name='movie_details')
    
]
