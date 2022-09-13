
from django.urls import path,include
from watchlistApp.api.views import WatchListAV,WatchDetailsAV,StreamPlatformsAV,StreamPlatformsDetailsAV
# from watchlistApp.api.views import movies,movie_details
urlpatterns = [
    # path('list/',movies,name='movie_list'),
    # path('list/<int:pk>/',movie_details,name='movie_details'),
    path('list/', WatchListAV.as_view(),name='watch_list'),
    path('list/<int:pk>/', WatchDetailsAV.as_view(),name='watch_details'),
    path('stream/', StreamPlatformsAV.as_view(),name='stream'),
    path('stream/<int:pk>/', StreamPlatformsDetailsAV.as_view(),name='Platforms_DetailsAV'),
]
