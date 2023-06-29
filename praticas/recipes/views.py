from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def contato (request):
    return (request, 'contato.html')

def home (request):
    return render (request, 'recipes/home.html', context={
        'name': 'Arthur Alves',
    })


def sobre(request):
    return HttpResponse('my history are your history BABY')
