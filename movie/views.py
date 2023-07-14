from django.shortcuts import render
from django.http  import HttpResponse
from .models import Movie

#form으로 날리자나요 request.Get.get('searchMovie') 
#미션 임파서블이 넘겨오면 저기로 넘어옴 
def home(request):
    searchTerm = request.GET.get('searchMovie')
    movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm,'movies': movies})


def about(request):
    return HttpResponse('<h1>About</h1>')


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html',{'email':email})

