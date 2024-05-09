from django.urls import path
from . import views

urlpatterns =[path('show/',views.display,name='display'),
path('myplayer/',views.myplayer_list, name='myplayer_list')]
