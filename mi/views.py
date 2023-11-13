from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def bumbra(request):
    return render(request,'bumbra.html')

def rohith(request):
    return HttpResponse('<h1>rohith sharama</h1>')