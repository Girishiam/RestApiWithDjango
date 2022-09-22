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








# @api_view(['GET', 'POST'])
# def movies(request):
#     if request.method == 'GET':
#         movies = Movies.objects.all()
#         serializers = MovieSerializer(movies,many=True)
#         return Response(serializers.data)
    
#     elif request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    


# @api_view(['GET','PUT', 'DELETE'])
# def movie_details(request,pk):
#     if request.method =='GET':
#         try:
#             movies = Movies.objects.get(pk=pk)
#         except Movies.DoesNotExist:
#             return Response({"Error":"Movie Not Found"},status = status.HTTP_404_NOT_FOUND)

#         serializers = MovieSerializer(movies)
#         return Response(serializers.data)

#     if request.method == 'PUT':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     if request.method == 'DELETE':
#         movies = Movies.objects.get(pk=pk)
#         movies.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)






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


# class ReviewsList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Reviews.objects.all()
#     serializer_class = ReviewsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class ReviewsDetails(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = Reviews.objects.all()
#     serializer_class = ReviewsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

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

    # def list(self, request):
    #     queryset = StreamPlatforms.objects.all()
    #     serializer = StreamPlatformsSerializer(queryset, many=True,context={'request':request})
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = StreamPlatforms.objects.all()
    #     watchList = get_object_or_404(queryset, pk=pk)
    #     serializer = StreamPlatformsSerializer(watchList,context={'request':request})
    #     return Response(serializer.data)

    # def create(self,request):
    #     serializer = StreamPlatformsSerializer(data=request.data,context={'request':request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)

