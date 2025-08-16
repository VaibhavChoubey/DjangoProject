from django.contrib import admin
from NewApp.models import NameDetails

# Register your models here.

class ModelList(admin.ModelAdmin):
     list_display = ['Name','Surname','Address','Qualification']



admin.site.register(NameDetails, ModelList)