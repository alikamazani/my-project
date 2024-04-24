from django.urls import path

from . import views

urlpatterns = [
    path('get-informations-synoptic', views.getInfoSynop, name='getinfosynop'),
    path('get-informations-climatology', views.getInfoClima, name='getinfoclima'),
    path('get-informations-agriculture', views.getInfoAgric, name='getinfoagric'),
]
