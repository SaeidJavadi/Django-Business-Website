from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('base.urls', namespace='base')),
                  path('accounts/', include('accounts.urls', namespace='accounts')),
                  re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_URL}),
                  # re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
              ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'مدیریت'
admin.site.site_title = 'پنل مدیریت'
admin.site.index_title = 'به پنل مدیریت خوش آمدید'
