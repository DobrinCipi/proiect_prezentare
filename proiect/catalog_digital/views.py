from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html", {})

def contact(request):
    return render(request, "contact.html", {})

def about(request):
    return render(request, "about.html", {})

def index(request):
    return render(request, "index.html", {})

def classs(request):
    return render(request, "class.html", {})

def team(request):
    return render(request, "team.html", {})