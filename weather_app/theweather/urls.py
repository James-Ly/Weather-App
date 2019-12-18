from django.urls import path
from . import views

app_name = 'theweather'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<city_name>/', views.delete_city, name='delete_city')
]
