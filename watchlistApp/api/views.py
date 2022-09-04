from watchlistApp.models import Movies
from watchlistApp.api.serializers import MovieSerializer
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

class MovieList(APIView):

    def get(self,request):
        movies = Movies.objects.all()
        serializers = MovieSerializer(movies,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class MovieDetails(APIView):
    def get(self,request,pk):
        try:
            movies = Movies.objects.get(pk=pk)
        except Movies.DoesNotExist:
            return Response({"Error":"Movie Not Found"},status = status.HTTP_404_NOT_FOUND)

        serializers = MovieSerializer(movies)
        return Response(serializers.data)

    def put(self,request,pk):

        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,pk):
        movies = Movies.objects.get(pk=pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


