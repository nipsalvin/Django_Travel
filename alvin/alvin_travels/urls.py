#create url.py for url mapping

from django.urls import path #import url paths from main urls(django.urls/alvin.urls)
from . import views

urlpatterns = [
    path('',views.index, name='index')
    #views.home calls 'home' function from 'views.py'
]

