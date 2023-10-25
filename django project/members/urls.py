#urls index
from django.urls import path
from . import views

urlpatterns = [  
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('jadwal_m/', views.jadwal_m, name='jadwal_m'),
    path('jadwal_t/', views.jadwal_t, name='jadwal_t'),
    path('jadwal_t/', views.jadwal_t, name='jadwal_t'),
    path('jadwal_m/', views.jadwal_m, name='jadwal_m'),
    path('hiburan/', views.hiburan, name='hiburan'),
]
