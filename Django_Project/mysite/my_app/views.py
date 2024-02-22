from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is my_app App.")

def return_simple_html(request):
    my_pages = [{
        'page_1': 'FIFA World Cup Winners',
        'page_2': 'Most Expensive Artworks',
        'page_3': 'Fitness Level Estimation Poll',
        }]
    
    return render(request, 'child.html',
                  context={'my_pages':my_pages})

def football(request):
    return render(request, 'football.html')

def most_expensive_artworks(request):
    return render(request, 'most.html')

def fitness(request):
    return render(request, 'fitness.html')