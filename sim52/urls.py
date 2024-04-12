from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *

# admin.site.site_header = "Sena DataLake Admin"
# admin.site.site_title = "Sena DataLake Admin"
# admin.site.index_title = "Welcome To Sena DataLake Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    #path('', include('lectivas.urls')),
    path('', include('productivas.urls')),

    path('', home, name='home'),
    path('privacy', privacy, name='privacy'),
    path('condiciones', condiciones, name='condiciones'),
    path('haveasData', haveasData, name='haveasData'),

    # path('page401', page401, name='page401'),
    path('page501', page501, name='page501'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 401 Unauthorized
# 403 Forbidden
# 404 Not Found