from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tutorials/',include('tutorials.urls')),
    path('about/',views.about),
    path('',views.homepage)

]




urlpatterns+= staticfiles_urlpatterns()



