from django.urls import path
from . import views


app_name = 'cddfrontend'
urlpatterns =[
    path('',views.placeListMap,name='placeslist_map'),
]