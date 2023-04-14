from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Elevi


# Create your views here.
def home(request):
    return render(request, "index.html", {})

def contact(request):
    if request.method == "POST":
        name_form = request.POST['name_form']
        email_form = request.POST['email_form']
        subject_form = request.POST['subject_form']
        message_form = request.POST['message_form']  
        
        # send an email 
        
        send_mail(
            name_form,
            message_form,
            email_form,
            ['schoolmy316@gmail.com'],    
        )
                
        return render(request, "contact.html", {'name_form': name_form})
    else:
        return render(request, "contact.html", {})
    


def about(request):
    return render(request, "about.html", {})

def index(request):
    return render(request, "index.html", {})

def classs(request):
    if request.method == "POST":
        name_elev = request.POST['class_name']
        name_parent = request.POST['class_parent']
        adresa_mail_elev = request.POST['class_email']
        phone_number = request.POST['class_phone']        
        # send an email 
        
        send_mail(
            name_elev,"Child of", name_parent,
            adresa_mail_elev,  phone_number
            ['schoolmy316@gmail.com'],    
        )
                
        return render(request, "class.html", {'name_form': name_elev})
    else:
        return render(request, "class.html", {})
    

def team(request):
    return render(request, "team.html", {})

def gallery(request):
    return render(request, "gallery.html", {})