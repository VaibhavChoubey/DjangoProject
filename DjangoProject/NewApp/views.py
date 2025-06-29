from django.shortcuts import render
from django.http import HttpResponse
from NewApp.models import NameDetails

# Create your views here.

def WelcomePageView(request):
    return HttpResponse("Welcome to homepage")

def UserName (request):
    UserDetails = NameDetails.objects.all()
    UserDetails_Dict = {'UserDetails' : UserDetails }
    return render(request , "Username.html" , context= UserDetails_Dict)