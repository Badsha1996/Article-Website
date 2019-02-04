from django.urls import path
from . import views
app_name="tutorials"
urlpatterns = [
    path('',views.all_tutorials,name='list'),
    path('<slug>/',views.details,name="detail"),

]
