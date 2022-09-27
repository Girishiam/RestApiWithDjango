from watchlistApp.models import WatchList,StreamPlatforms,Reviews
from watchlistApp.api.serializers import WatchListSerializer,StreamPlatformsSerializer,ReviewsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics,mixins,status,viewsets
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from watchlistApp.api.permissions import AdminOrReadOnly



class WatchListAV(APIView):

    def get(self,request):
        movies = WatchList.objects.all()
        serializers = WatchListSerializer(movies,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailsAV(APIView):
    def get(self,request,pk):
        try:
            movies = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"Error":"Watchlist Not Found"},status = status.HTTP_404_NOT_FOUND)

        serializers = WatchListSerializer(movies)
        return Response(serializers.data)

    def put(self,request,pk):

        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,pk):
        movies = WatchList.objects.get(pk=pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformsAV(APIView):
    def get(self,request):
        platform = StreamPlatforms.objects.all()
        serializers = StreamPlatformsSerializer(platform,many=True,context={'request':request})
        return Response(serializers.data)

    def post(self,request):
        serializer = StreamPlatformsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class StreamPlatformsDetailsAV(APIView):
    def get(self,request,pk):
        try:
            platforms = StreamPlatforms.objects.get(pk=pk)
        except StreamPlatforms.DoesNotExist:
            return Response({"Error":"Platforms Not Found"},status = status.HTTP_404_NOT_FOUND)

        serializers = StreamPlatformsSerializer(platforms,context={'request':request})
        return Response(serializers.data)

    def put(self,request,pk):

        serializer = StreamPlatformsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,pk):
        platforms = StreamPlatforms.objects.get(pk=pk)
        platforms.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ReviewsList(generics.ListAPIView):
    # queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Reviews.objects.filter(watchlist=pk)

class ReviewsCreate(generics.CreateAPIView):
    serializer_class = ReviewsSerializer

    def get_queryset(self):
        return Reviews.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Reviews.objects.filter(watchlist=watchlist, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError('You already submitted your review')
        



        if watchlist.numberOfRating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating'])/2

        watchlist.numberOfRating = watchlist.numberOfRating + 1

        watchlist.save()

        serializer.save(watchlist=watchlist,review_user=review_user)




class ReviewsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [AdminOrReadOnly]

class StreamPlatformsVS(viewsets.ModelViewSet):
    queryset = StreamPlatforms.objects.all()
    serializer_class = StreamPlatformsSerializer

