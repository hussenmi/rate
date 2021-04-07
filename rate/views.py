from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'rate/home.html')
def about(request):
    return render(request, 'rate/about.html')