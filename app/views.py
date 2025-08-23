from django.shortcuts import render
import requests, os
# Create your views here.
def index(request):
    city = request.GET.get('city' , 'Jalgaon')
    API_KEY = os.getenv('API_KEY')
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    api_response = requests.get(api_url).json()
    temprature = api_response['main']['temp']
    city_name = api_response['name']
    country = api_response['sys']['country']
    speed = api_response['wind']['speed']
    humidity = api_response['main']['humidity']
    main = api_response['weather'][0]['main']
    description = api_response['weather'][0]['description']
    icon = api_response['weather'][0]['icon']
    icon_url = f'https://openweathermap.org/img/wn/{icon}@2x.png'
     
    return render(request, 'index.html', {'temprature': temprature, 'city_name':city_name, 'country':country ,'speed':speed, 'humidity' :humidity, 'main':main, 'icon_url':icon_url, 'description': description})