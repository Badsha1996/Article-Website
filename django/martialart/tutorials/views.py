from django.shortcuts import render
from .models import Tutorial
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



# Create your views here.

def all_tutorials(request):
    tutorials=Tutorial.objects.all().order_by('date')
    return render(request,"tutorials/tutorials.html",{'tutorials':tutorials})


@login_required(login_url='/accounts/login/')
def details(request,slug):
    tutorial=Tutorial.objects.get(slug=slug)
    return render(request,'tutorials/frame.html',{'tutorial':tutorial})