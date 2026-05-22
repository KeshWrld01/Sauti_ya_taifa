# sauti_ya_taifa/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('donations/', include('donations.urls')),
    path('school/', include('school.urls')),
    path('say-names/', include('say_names.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)