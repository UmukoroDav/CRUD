from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('base/', views.base, name='appbase' ),
    path('home/', views.index, name='appindex' ),
    path('register/', views.register, name='appregister'),
    path('index/', views.home, name="apphome"),
    path('logout/', views.logout_g, name='applogout'),
    path('record/<int:pk>/', views.record, name='apprecord'),
    path('delete/<int:pk>/', views.delete, name='appdelete'),
    path('add/', views.add_record, name='appadd'),
    path('update/<int:pk>', views.update_record, name='appupdate'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
