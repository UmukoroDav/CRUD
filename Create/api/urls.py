from django.urls import path
from . import views

urlpatterns = [
    path('', views.getroutes), 
    path('record/', views.getrecords), 
    path('record/<int:pk>', views.getrecord), 
]
