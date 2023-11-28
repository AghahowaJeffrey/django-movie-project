from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .serializer import MovieSerializer
from .models import Movie
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def movie_list(request):

    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse({'drinks': serializer.data})
    
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, id):

    try:
       movie = Movie.objects.get(pk=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        pass

# def movies(request):
#     data = Movie.objects.all
#     return render(request, 'movies/movies.html', {'movies': data}) 

# def home(request):
#     return HttpResponse('Home page')

# def detail(request, id):
#     data = Movie.objects.get(pk=id)
#     return render(request, 'movies/detail.html', {'movie': data})

# def add(request):
#     title = request.POST.get('title')
#     year = request.POST.get('year')

#     if title and year:
#         movie = Movie(title=title, year=year)
#         movie.save()
#         return HttpResponseRedirect('/movies')
    
#     return render(request, 'movies/add.html')

# def delete(request, id):
#     try:
#         movie = Movie.objects.get(pk=id)
#     except:
#         raise Http404('Movie does not exist')
#     movie.delete()
#     return HttpResponseRedirect('/movies')

# def update(request, id):
#     movie = Movie.objects.get(pk=id)
    
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         year = request.POST.get('year')

#         if title and year:
#             # Update the attributes
#             movie.title = title
#             movie.year = year
#             movie.save()
#             return HttpResponseRedirect('/movies')
    
#     return render(request, 'movies/update.html')