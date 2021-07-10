from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('homepage')
    return render(request, 'index2.html')