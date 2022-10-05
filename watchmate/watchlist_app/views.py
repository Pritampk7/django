from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from .models import Watchlist, Streamplatform, Review
from django.http import JsonResponse
from .serializers import Watchlistserializers, PlatformSerializers, ReviewSerializer
from rest_framework import status, generics, mixins
from rest_framework.decorators import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .permissions import AdminOnReadOnly, EditUserOrReadOnly


# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = movieserializers(movies, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = movieserializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try:
#             movies = Movie.objects.get(pk=pk)
#         except KeyError:
#             return Response({'error': f'movies not found'}, status=status.HTTP_404_NOT_FOUND)
#         print(movies)
#         serializer = movieserializers(movies)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = movieserializers(movie, data=request.data, status=status.HTTP_200_OK)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'DELETE':
#         movies = Movie.objects.get(pk=pk)
#         movies.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):
    permission_classes = [AdminOnReadOnly]

    def get(self, request):
        movies = Watchlist.objects.all()
        serializer = Watchlistserializers(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Watchlistserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):
    permission_classes = [EditUserOrReadOnly]

    def get(self, request, pk):
        try:
            movies = Watchlist.objects.get(pk=pk)
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        print(movies)
        serializer = Watchlistserializers(movies)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = Watchlist.objects.get(pk=pk)
        serializer = Watchlistserializers(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(request, pk):
        movies = Watchlist.objects.get(pk=pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatform(APIView):
    def get(self, request):
        platform = Streamplatform.objects.all()
        serializer = PlatformSerializers(platform, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlatformSerializers(data=request.dat)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetails(APIView):

    def get(self, request, pk):
        try:
            stream = Streamplatform.objects.get(pk=pk)
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        print(stream)
        serializer = PlatformSerializers(stream)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = Streamplatform.objects.get(pk=pk)
        serializer = PlatformSerializers(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(request, pk):
        movies = Streamplatform.objects.get(pk=pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = Watchlist.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)

        if review_queryset.exists:
            raise ValidationError("You have already reviewed this movie")

        serializer.save(watchlist=watchlist, review_user=review_user)

class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewDetail(mixins.ListModelMixin, mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

