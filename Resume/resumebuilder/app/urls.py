from django.urls import path
from .views import *


urlpatterns = [
   
    path('personalinfoview/',personalinfoview,name='personalinfoview'),
    path('download/',download,name='download'),
    path('sendemailview/',sendemailview,name='sendemailview'),
    path('updateresume/<int:id>',updateresume,name='updateresume'),

    
    ]
