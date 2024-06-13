from django.db import models
from django.urls import reverse
# Create your models here.

class School(models.Model):
    Sname = models.CharField(max_length=100)
    Sprincipal = models.CharField(max_length=100)
    Slocation = models.CharField(max_length=100)

    def __str__(self) :
        return self.Sname
    
    # to create Canonical urls we use get_absolute_url()
    def get_absolute_url(Self):
        return reverse('detail',kwargs={'pk':Self.pk})
    

class Student(models.Model):
    Stname = models.CharField(max_length=100)
    Stage = models.IntegerField(max_length=100)
    Sname = models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')

    #related_name is used to refer Child Table data w/o using child table data but using parent table object and related_name

    def __str__(self) :
        return self.Stname
    
