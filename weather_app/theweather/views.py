from django.shortcuts import render
import requests
from . import models, forms


# Create your views here.

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=ebe66a355c7e37e84f393b83f4d2e1a6'
    err_msg = ''
    message = ''
    message_class = ''
    if request.method == 'POST':
        city_form = forms.CityForm(data=request.POST)
        if city_form.is_valid():
            new_city = city_form.cleaned_data['name']
            existing_city_count = models.City.objects.filter(name=new_city).count()
            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                print(r)
                if r['cod'] == 200:
                    city_form.save()
                else:
                    err_msg = 'City does not exist in the world'
            else:
                err_msg = 'City already exists in the database!'
        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully'
            message_class = 'is-sucess'

    print(err_msg)
    city_form = forms.CityForm()
    cities = models.City.objects.all()
    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    context = {'city_weather': weather_data, 'form': city_form, 'message': message, 'message_class': message_class}
    return render(request, 'weather/weather.html', context)
