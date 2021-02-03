from django.urls import path
from base import views
from django.conf import settings
from django.conf.urls.static import static

app_name= 'base'

urlpatterns = [
    path('', views.index, name='index'),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
