from django.db import models

# Create your models here.
class NameDetails(models.Model):
    Name = models.TextField(("Name"))
    Surname = models.TextField(("Surname"))
    Address = models.CharField(("Address"), max_length=50)
    Qualification = models.CharField(("Qualification"), max_length=50)
