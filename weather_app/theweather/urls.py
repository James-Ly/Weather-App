from django.urls import path
from . import views

app_name = 'theweather'

urlpatterns = [
    path('', views.index, name='index'),
]
