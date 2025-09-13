from django import forms

class PerformanceDetailsForm(forms.Form):
    FirstName=  forms.CharField()
    Marks = forms.FloatField()