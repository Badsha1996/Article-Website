from django.urls import path
from . import views

app_name="videos"

urlpatterns = [
    path('',views.all_videos,name='list'),
    path('<slug>/',views.vid,name="detail"),

]
