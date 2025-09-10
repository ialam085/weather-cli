import requests

def get_weather(city):
    api_key = "93ba6b8a1f1c8741bd71801edd005b70"
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(base_url)
        data = response.json()

        if data.get('cod') == 200:
            return data
        else:
            return {"error": data.get('message', 'Unknown error')}
    except requests.RequestException as e:
        return {"error": f"Network error: {e}"}

# Optional: for direct run
if __name__ == "__main__":
    city = input("Enter city name: ")
    result = get_weather(city)
    if "error" in result:
        print(result["error"])
    else:
        print(f"Weather in {city}:")
        print(f"Description: {result['weather'][0]['description']}")
        print(f"Temperature: {result['main']['temp']} °C")
        print(f"Humidity: {result['main']['humidity']}%")
        print(f"Wind Speed: {result['wind']['speed']} m/s")
