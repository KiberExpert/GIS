from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='index'),
    path('login/',login,name='login')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)