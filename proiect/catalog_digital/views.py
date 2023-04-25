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
            f'{name_form}, {email_form}',
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
    if request.method == "POST":
        name_registration = request.POST['news_name']
        email_registration = request.POST['news_email']

        
           
        # send an email 
        
        send_mail(
            'Newsletter Registration',
            name_registration,
            email_registration,
            ['schoolmy316@gmail.com']
        )
                
        return render(request, "index.html", {})
    else:
        return render(request, "index.html", {})
    

def classs(request):
    if request.method == "POST":
        name_elev = request.POST['class-name']
        name_parent = request.POST['class_parent']
        mail_addres = request.POST['class-email']
        phone_number = request.POST['class-phone']     
        class_selection = request.POST['class-selection']

        
           
        # send an email 
        
        send_mail(
            'Class Registration',
            f'Child Name: {name_elev}, Parent Name: {name_parent}, Email Adress: {mail_addres}, Phone Number:{phone_number},Selected Class:{class_selection}',
            mail_addres,
            ['schoolmy316@gmail.com']
        )
                
        return render(request, "class.html", {'class_parent': name_parent })
    else:
        return render(request, "class.html", {})
    

def team(request):
    if request.method == "POST":
        name_registration = request.POST['news_name']
        email_registration = request.POST['news_email']

        
           
        # send an email 
        
        send_mail(
            'Newsletter Registration',
            name_registration,
            email_registration,
            ['schoolmy316@gmail.com']
        )
                
        return render(request, "team.html", {})
    else:
        return render(request, "team.html", {})

def gallery(request):
    if request.method == "POST":
        name_registration = request.POST['news_name']
        email_registration = request.POST['news_email']

        
           
        # send an email 
        
        send_mail(
            'Newsletter Registration',
            name_registration,
            email_registration,
            ['schoolmy316@gmail.com']
        )
                
        return render(request, "gallery.html", {})
    else:
        return render(request, "gallery.html", {})
    

def test(request):
    return render(request, "test.html", {})

def contact_registration(request):
    if request.method == "POST":
        name_registration = request.POST['news_name']
        email_registration = request.POST['news_email']

        
           
        # send an email 
        
        send_mail(
            'Newsletter Registration',
            name_registration,
            email_registration,
            ['schoolmy316@gmail.com']
        )
                
        return render(request, "contact.html", {})
    else:
        return render(request, "contact.html", {})
    
def class_registration(request):
    if request.method == "POST":
        name_registration = request.POST['news_name']
        email_registration = request.POST['news_email']

        
           
        # send an email 
        
        send_mail(
            'Newsletter Registration',
            name_registration,
            email_registration,
            ['schoolmy316@gmail.com']
        )
                
        return render(request, "class.html", {})
    else:
        return render(request, "class.html", {})