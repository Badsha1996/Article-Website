from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from accounts import views as account_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/',include('accounts.urls')),
    path('tutorials/',include('tutorials.urls')),
    path('videos/',include('videos.urls')),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('home/', views.home, name='home'),
    path('',account_views.login_view,name="index"),

]




urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



