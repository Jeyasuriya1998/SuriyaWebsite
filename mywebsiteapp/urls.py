from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="start"),
    path('welcome', views.welcome, name="welcome"),
    path('profile', views.profile, name="profile"),
    path('formal_resume', views.formal_resume, name="formal_resume"),
    path('smart_resume', views.smart_resume, name="smart_resume"),
    path('resumepdf', views.resumepdf, name="resumepdf"),
    path('resume', views.resume, name="resume"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('project/<str:pk>', views.project, name="project"),
    path('achievement\<str:pk>', views.achievement, name="achievement"),
   
    path('contact', views.contact, name="contact"),
    path('contact_me', views.contact_me, name="contact_me"),
    
    path('sent_email', views.sendEmail, name="sent_email"),
    ]