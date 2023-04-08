from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html", {})

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']  
        return render(request, "contact.html", {'name': name})
    else:
        return render(request, "contact.html", {})

def about(request):
    return render(request, "about.html", {})

def index(request):
    return render(request, "index.html", {})

def classs(request):
    return render(request, "class.html", {})

def team(request):
    return render(request, "team.html", {})

def gallery(request):
    return render(request, "gallery.html", {})