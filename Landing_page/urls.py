from django.urls import path
from .views import  HomeInformation

app_name = 'homepage'

urlpatterns = [
    path('', HomeInformation.as_view(), name='information'),
]