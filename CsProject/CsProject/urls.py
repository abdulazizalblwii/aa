from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('baseApp.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


admin.site.site_header = 'CS 393 Administration'