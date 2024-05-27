from django.urls import path
from .views import *


urlpatterns = [
   
     path('home/',home,name='home'),
     path('aboutus/',aboutus,name='aboutus'),
     path('contactus/',contactus,name='contactus'),
     path('contactdetails/',contactdetails,name='contactdetails'),
     path('kitcheninventory/',kitcheninventory,name='kitcheninventory'),
     path('addinventory/',addinventory,name='addinventory'),
     path('showinv/',showinv,name='showinv'),
     path('updateinv/<int:id>',updateinv,name='updateinv'),
     path('deleteinv/<int:id>',deleteinv,name='deleteinv'),
     path('monthlyinv/',monthlyinv,name='monthlyinv'),
     path('printlist/',printlist,name='printlist'),


]