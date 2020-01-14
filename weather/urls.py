from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage,name="homepage"),
    path('hourly_forecast/', views.hourly_forecast,name="hourly_forecast"),
    path('days_forecast/', views.daysforecast,name="5_days_forecast"),
   
    path('weather_alerts/', views.weather_alerts,name="weather_alerts"),
 ] 