from flask import Flask, render_template, request
import requests
from datetime import datetime
import mysql.connector

API_KEY = '4f517007705b3f5c606873c1db94f27a'  
DB_CONFIG = {
    'user': 'root',
    'password': 'Zakshada@26',
    'host': 'localhost',
    'database': 'weather_db'
}

app = Flask(__name__)

def fetch_weather_data(city):
    """Fetch weather data from OpenWeatherMap API."""
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    weather_data = fetch_weather_data(city)
    
    if weather_data:
        weather_info = {
            'city': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'feels_like': weather_data['main']['feels_like'],
            'humidity': weather_data['main']['humidity'],
            'wind_speed': weather_data['wind']['speed'],
            'weather_condition': weather_data['weather'][0]['description'],
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return render_template('weather_result.html', weather=weather_info)
    else:
        return render_template('index.html', error="City not found.")

if __name__ == '__main__':
    app.run(debug=True)
