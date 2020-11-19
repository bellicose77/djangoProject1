from django.conf.urls import include
from django.urls import path
from My_firstapp import views

urlpatterns=[
    path('', views.home, name='home'),
    path('',views.index, name='about'),
]