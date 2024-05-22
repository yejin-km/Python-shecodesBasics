import requests
from rich import print
from datetime import datetime

def welcome_message():
    """displays welcome message"""
    print("[dark_magenta underline bold]Welcome to my weather app[/dark_magenta underline bold]")
    
def display_temperature(day, temperature, unit='C'):
    """displays day and temperature"""
    print(f"[deep_sky_blue3]{day}[/deep_sky_blue3]: [white]{temperature}°{unit}[/white] {convert_to_fahrenheit(temperature)}")
    
def convert_to_fahrenheit(temperature):
    """convert celsius to fahrenheit"""
    fahrenheit = f"[green italic]({round((temperature * 9/5) + 32)}°F)[/green italic]"
    return fahrenheit

def display_current_weather():
    """displays current weather"""
    api_key = "2046c535afeb092fo82f1d306d8a2b2t"
    api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"
    
    response = requests.get(api_url)
    current_weather = response.json()

    temperature = round(current_weather['temperature']['current'])
    
    display_temperature("Today: ", temperature)
    
    
def display_forecast():
    """displays forecast"""
    api_key = "2046c535afeb092fo82f1d306d8a2b2t"
    api_url = f"https://api.shecodes.io/weather/v1/forecast?query={city}&key={api_key}"
    
    response = requests.get(api_url)
    days = response.json()
    
    print("\n[green_yellow underline bold]Forecast:[/green_yellow underline bold]")
    for day in days['daily']:
        timestamp = day['time']
        date = datetime.fromtimestamp(timestamp)
        formatted_day = date.strftime("%A")
        temperature = round(day['temperature']['day'])

        if date.date() != datetime.today().date():
            display_temperature(formatted_day, temperature)


welcome_message()
city = input("Enter a city: ")

# validate user input
while not city:
    city = input("Try again. Enter a city: ")
        
display_current_weather()
display_forecast() 

print("\n[medium_purple1]This app was built by Yejin Kim[/medium_purple1]")