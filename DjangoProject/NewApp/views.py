from django.shortcuts import render
from django.http import HttpResponse
from NewApp.models import NameDetails

# Create your views here.

def WelcomePageView(request):
    return HttpResponse("Welcome to homepage")

def UserName (request):
    UserDetails = NameDetails.objects.all()
    Name = NameDetails.objects.get(Name= 'Vaibhav')
    UserDetails_Dict = {'UserDetails' : UserDetails, 'Name': Name.Name }
    return render(request , "Username.html" ,  context = UserDetails_Dict)