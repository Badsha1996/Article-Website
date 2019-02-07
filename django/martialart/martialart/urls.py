from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('tutorials/',include('tutorials.urls')),
    path('videos/',include('videos.urls')),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('',views.homepage,name="index"),
]




urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



