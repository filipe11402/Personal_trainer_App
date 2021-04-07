from django.urls import path
from .views import loginview


app_name = 'accounts'

urlpatterns = [
    path('login/', loginview, name='login'),
]