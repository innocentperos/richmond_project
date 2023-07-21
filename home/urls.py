from django.urls import path,include
from home.views import *
from car_dealer_portal import *
from customer_portal import *

urlpatterns = [
    path("",home_page),
]
