from django.shortcuts import render
from django.views.generic import DetailView,ListView
from app.models import *
from django.http import HttpResponse
# Create your views here.


class SchoolList(ListView):
    model=School
    context_object_name='schools'
    #queryset=School.objects.filter(Scname='Qspiders')
    #ordering=['Scname']

def wish(request,n):
    return HttpResponse(f'Hai {n} How are U')



class SchoolDetail(DetailView):
    model= School
    context_object_name = 'schoolobject'
