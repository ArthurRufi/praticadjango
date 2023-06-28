from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def contato (request):
    return HttpResponse('Contato BABY')


def home (request):
    return HttpResponse('welcome to the home BABY')


def sobre(request):
    return HttpResponse('my history are your history BABY')
