from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ab(request):
    return render(request,'ab.html')

def virat(request):
    return HttpResponse('<h1>virat kohli</h1>')