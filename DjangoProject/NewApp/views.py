from django.shortcuts import render
from django.http import HttpResponse
from NewApp.models import NameDetails
from NewApp.forms import PerformanceDetailsForm, NameDetailsForm
import inspect
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def WelcomePageView(request):
    return HttpResponse("Welcome to homepage")

def UserName (request):
    UserDetails = NameDetails.objects.all()
    Name = NameDetails.objects.get(Name= 'Vaibhav')
    UserDetails_Dict = {'UserDetails' : UserDetails, 'Name': Name.Name }
    return render(request , "Username.html" ,  context = UserDetails_Dict)

def PerformanceDetailsView(request):
    
    form = PerformanceDetailsForm()
    if request.method == 'POST':
        form = PerformanceDetailsForm(request.POST)
        if form.is_valid():
            logger.info("Form is valid")
            FirstName = form.cleaned_data['FirstName']
            PassStatus = form.cleaned_data['PassStatus']
            logger.info(f"Email : {form.cleaned_data['email']}")
            logger.info(f"Pass Status of {FirstName} is {PassStatus}")

        else:
            logger.info("Data entered is invalid ")
        
    return render(request , "PerformanceDetails.html" ,{'form': form} )

def ActionsPageView(request):
    return render(request , 'ActionsPage.html' )

def AddNewEntryView(request):
    form = NameDetailsForm()
    if request.method == 'POST':
        form = NameDetailsForm(request.POST)
        if form.is_valid:
            form.save()
            return ActionsPageView(request)
        else:
            logger.info("form submitted is invalid")
    return render(request, 'AddNewEntry.html', {'form': form})

def ViewAllEntriesView(request):
    UserNames = NameDetails.objects.all()
    return render(request, 'ViewAllEntries.html', {'UserDetails' : UserNames} )
