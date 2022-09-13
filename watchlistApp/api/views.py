from watchlistApp.models import WatchList,StreamPlatforms
from watchlistApp.api.serializers import WatchListSerializer,StreamPlatformsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView


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
        serializers = StreamPlatformsSerializer(platform,many=True)
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

        serializers = StreamPlatformsSerializer(platforms)
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
