from django import forms
from django.core.exceptions import ValidationError
from NewApp import models as NameDetailModels
from django.core.validators import MinLengthValidator, MaxLengthValidator
import logging

logger = logging.getLogger(__name__)

class PerformanceDetailsForm(forms.Form):
    PassStatus = [('pass', 'PASS'),('fail', 'FAIL')]
    FirstName=  forms.CharField(validators= [MinLengthValidator(5),MaxLengthValidator(20)])
    Marks = forms.FloatField()
    email = forms.CharField(required= False)
    PassStatus = forms.CharField(widget = forms.Select(choices=PassStatus))

    def clean_FirstName(self):
        FirstName = self.cleaned_data.get('FirstName')

        if len(FirstName) > 20:
            logger.info("FirstName's length exceeds the limitation of 20")
            raise ValidationError("Max length allowed is 20")
        return FirstName
    
    def clean(self):
        FormData=  super().clean()
        EmailAddress = FormData['email']
        if EmailAddress.find('@') == -1:
            raise ValidationError("Email Address is Invalid")
        
class NameDetailsForm(forms.ModelForm):
    class Meta:
        model = NameDetailModels.NameDetails
        fields = '__all__'
        