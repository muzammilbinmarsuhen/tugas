# urls utama website 
from django.contrib import admin
from django.urls import include, path
from members.views import *

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('jadwal_m/', jadwal_m, name='jadwal_m'),
    path('jadwal_t/', jadwal_t, name='jadwal_t'),
    path('jadwal_t/', jadwal_t, name='jadwal_t'),
    path('jadwal_m/', jadwal_m, name='jadwal_m'),
    path('hiburan/', hiburan, name='hiburan'),
    path('admin/', admin.site.urls),
]