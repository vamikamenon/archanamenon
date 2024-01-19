from django.http import HttpResponse
from . models import Movies
from django.shortcuts import render, redirect
from . forms import MovieForm

# Create your views here.


def index(request):
    movie=Movies.objects.all()
    context={'movie_list':movie}
    return render(request,'index.html',context)


def details(request,movie_id):
    movie1=Movies.objects.get(id=movie_id)
    return render(request, "detail.html", {'mve': movie1})


def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movie=Movies(name=name,desc=desc,year=year,img=img)
        movie.save()
        return redirect('/')
    return render(request,'add_movie.html')


def update(request, id):
    mve = Movies.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=mve)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':mve})


def delete(request, id):
    if request.method=='POST':
        movie1=Movies.objects.get(id=id)
        movie1.delete()
        return redirect('/')
    return render(request,'delete.html')
