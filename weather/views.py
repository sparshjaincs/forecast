from django.shortcuts import render
import requests
# Create your views here.
def homepage(request):
    context = {}
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"
    
    headers = {
    'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com",
    'x-rapidapi-key': "7a19c1191dmsh541ae74fcd60759p1c1d68jsnfe0e28b393c8"
    }
    if request.method == 'POST':
        lat = float(request.POST.get('latitude'))
        lon = float(request.POST.get('longitude'))
        querystring = {"lang":"en","lon":f"{lon}","lat":f"{lat}"}
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
        except Exception as exp:
            context['message'] = exp
        
        if response.status_code == 200:
            response = response.json()
            dictionary= {
            'pressure':response.get('data')[0].get('pres'),
            'city_name':response.get('data')[0].get('city_name'),
            'wind_speed':response.get('data')[0].get('wind_spd'),
            'wind_dir':response.get('data')[0].get('wind_cdir_full'),
            'sunset':response.get('data')[0].get('sunset'),
            'sunrise':response.get('data')[0].get('sunrise'),
            'dew_point':response.get('data')[0].get('dewpt'),
            'temprature':response.get('data')[0].get('temp'),
            'weather':response.get('data')[0].get('weather').get('description'),
            'timezone':response.get('data')[0].get('timezone'),
            }
            context['dictionary'] = dictionary
        else:
            context['message2'] = "Incorrect Latitude and Longitude"
    

    return render(request,'weather/homepage.html',context)



def hourly_forecast(request):
    context = {}
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/hourly"
    url1 = "https://weatherbit-v1-mashape.p.rapidapi.com/current"
    headers = {
        'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com",
        'x-rapidapi-key': "7a19c1191dmsh541ae74fcd60759p1c1d68jsnfe0e28b393c8"
        }
    if request.method == 'POST':
        dictionary = {}
        lat = float(request.POST.get('latitude'))
        lon = float(request.POST.get('longitude'))
        querystring = {"lang":"en","lon":f"{lon}","lat":f"{lat}"}
        hours = abs(int(request.POST.get('hours')))
        querystring1 = {"lang":"en","hours":f"{hours}","lat":"54.33","lon":"53.22"}
        context['hours'] = hours
        
        try:
            response = requests.request("GET", url, headers=headers, params=querystring1)
            response1 = requests.request("GET", url1, headers=headers, params=querystring)
        except Exception as exp:
            context['message'] = exp
        if response1.status_code == 200:
            response1 = response1.json()
            dictionary1 = {
                'timezone':response1.get('data')[0].get('timezone'),
                'city_name':response1.get('data')[0].get('city_name'),

            }
            context['dictionary1'] = dictionary1
        else:
            context['message2'] = "Incorrect Latitude and Longitude"

        if response.status_code == 200:
            response = response.json()
            response = response.get('data')[hours-1]
            dictionary= {
            'pressure':response.get('pres'),
            #'city_name':response.get('data')[0].get('city_name'),
            'wind_speed':response.get('wind_spd'),
            'wind_dir':response.get('wind_cdir_full'),
            'solar_radiation':response.get('solar_rad'),
            'ozone':response.get('ozone'),
            'dew_point':response.get('dewpt'),
            'precipitation':response.get('precip'),
            'temprature':response.get('temp'),
            'weather':response.get('weather').get('description'),
            #'timezone':response.get('data')[0].get('timezone'),
            }
        else:
            context['message2'] = "Incorrect Latitude and Longitude"
        context['dictionary'] = dictionary



    return render(request,'weather/hourly_forecast.html',context)


def daysforecast(request):
    context = {}
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/daily"
    url1 = "https://weatherbit-v1-mashape.p.rapidapi.com/current"
    headers = {
        'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com",
        'x-rapidapi-key': "7a19c1191dmsh541ae74fcd60759p1c1d68jsnfe0e28b393c8"
        }
    if request.method == 'POST':
        dictionary = {}
        lat = float(request.POST.get('latitude'))
        lon = float(request.POST.get('longitude'))
        querystring = {"lang":"en","lon":f"{lon}","lat":f"{lat}"}
        day = abs(int(request.POST.get('day')))
        
        context['hours'] = day
        
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
            response1 = requests.request("GET", url1, headers=headers, params=querystring)
        except Exception as exp:
            context['message'] = exp
        if response1.status_code == 200:
            response1 = response1.json()
            dictionary1 = {
                'timezone':response1.get('data')[0].get('timezone'),
                'city_name':response1.get('data')[0].get('city_name'),

            }
            context['dictionary1'] = dictionary1
        else:
            context['message2'] = "Incorrect Latitude and Longitude"

        if response.status_code == 200:
            response = response.json()
            response = response.get('data')[day-1]
            dictionary= {
            
            'pressure':response.get('pres'),
            #'city_name':response.get('data')[0].get('city_name'),
            'wind_speed':response.get('wind_spd'),
            'wind_dir':response.get('wind_cdir_full'),
            
            'ozone':response.get('ozone'),
            'dew_point':response.get('dewpt'),
            'precipitation':response.get('precip'),
            'temprature':response.get('temp'),
            'weather':response.get('weather').get('description'),
            #'timezone':response.get('data')[0].get('timezone'),
            }
        else:
            context['message2'] = "Incorrect Latitude and Longitude"
        context['dictionary'] = dictionary
    return render(request,'weather/fivedaysforecast.html',context)


def weather_alerts(request):
    return render(request,'weather/weather_alerts.html')