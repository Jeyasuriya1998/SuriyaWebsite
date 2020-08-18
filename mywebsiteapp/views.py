from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects, Achievements

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
    
def index(request):
    return render(request, "index.html")

def welcome(request):
    return render(request, "index.html")

def profile(request):
    return render(request, "profile.html")

def resume(request):
    return render(request, "resume.html")

def portfolio(request):
    projects = Projects.objects.all()
    achievements = Achievements.objects.all()
    
    context = {'achievements': achievements, 'projects':projects}
    return render(request, "portfolio.html", context)

def project(request, pk):
    project = Projects.objects.get(id=pk)
    
    context = {'project': project}
    return render(request, "project.html", context)

def achievement(request, pk):
    achieve = Achievements.objects.get(id=pk)
    
    context = {'achieve': achieve}
    return render(request, "achieve.html", context)


def contact(request):
    return render(request, "contact.html")

def formal_resume(request):
    return render(request, "formal_resume.html")

def smart_resume(request):
    return render(request, "smart_resume.html")

def resumepdf(request):
    return render(request, "resumepdf.html")

def contact_me(request):
    return render(request, "contact_me.html")

def sendEmail(request):
    
    if request.method == "POST":
        template = render_to_string('email_template.html',{
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
            })
        
        email = EmailMessage(
                request.POST['subject'],
                template,
                settings.EMAIL_HOST_USER,
                ['suriyajeyasuriya123@gmail.com'],
                )
        
        email.fail_silently = False
        email.send()
    return render(request, 'email_sent.html')