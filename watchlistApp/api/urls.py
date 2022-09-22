
from django.urls import path,include
from watchlistApp.api.views import (WatchListAV,WatchDetailsAV,StreamPlatformsAV,
                                    StreamPlatformsDetailsAV,ReviewsList,
                                    ReviewsDetails,StreamPlatformsVS,ReviewsCreate)


# from watchlistApp.api.views import movies,movie_details
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('stream', StreamPlatformsVS, basename='streamplatforms')






urlpatterns = [
    # path('list/',movies,name='movie_list'),
    # path('list/<int:pk>/',movie_details,name='movie_details'),

    path('list/', WatchListAV.as_view(),name='watch_list'),
    path('list/<int:pk>/', WatchDetailsAV.as_view(),name='watch_details'),

    path('',include(router.urls)),

    # path('stream/', StreamPlatformsAV.as_view(),name='stream'),
    # path('stream/<int:pk>/', StreamPlatformsDetailsAV.as_view(),name='streamplatforms-detail'),

    path('<int:pk>/reviews-create/', ReviewsCreate.as_view(),name='reviews-create'),
    path('<int:pk>/reviews/', ReviewsList.as_view(),name='reviews-list'),
    path('reviews/<int:pk>/',ReviewsDetails.as_view(),name='reviews-details'),

    # path('reviews/',ReviewsList.as_view(),name='reviews-list'),
    # path('reviews/<int:pk>/',ReviewsDetails.as_view(),name='reviews-list'),
]
