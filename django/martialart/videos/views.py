from django.shortcuts import render
from .models import Videos
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



# Create your views here.

def all_videos(request):
    videos=Videos.objects.all().order_by('date')
    return render(request,"videos/video.html",{'videos':videos})


@login_required(login_url='/accounts/login/')
def vid(request,slug):
    videos=Videos.objects.get(slug=slug)
    return render(request,'videos/frame.html',{'videos':videos})


