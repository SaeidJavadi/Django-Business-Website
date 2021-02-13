from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls', namespace='base')),
    path('accounts/', include('accounts.urls', namespace='accounts'))
]

admin.site.site_header = 'مدیریت'
admin.site.site_title = 'پنل مدیریت'
admin.site.index_title = 'به پنل مدیریت خوش آمدید'