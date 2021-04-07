from django.urls import path
from .views import *


app_name = 'training'

urlpatterns = [
    path('homepage/', indexview, name='homepage'),
]