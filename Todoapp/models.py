from django.db import models
from django.db.models import fields
from django.forms import ModelForm

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    eid  =   models.CharField(max_length=20)
    emobile = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"