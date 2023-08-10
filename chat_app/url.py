from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('<str:Broom>/',views.Room,name='Room'),
    path('checkview',views.checkview,name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:broom>/', views.getMessages, name='getMessages'),
]