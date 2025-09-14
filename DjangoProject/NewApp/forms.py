from django import forms

class PerformanceDetailsForm(forms.Form):
    PassStatus = [('pass', 'PASS'),('fail', 'FAIL')]
    FirstName=  forms.CharField()
    Marks = forms.FloatField()
    email = forms.CharField(widget= forms.EmailInput)
    PassStatus = forms.CharField(widget = forms.Select(choices=PassStatus))