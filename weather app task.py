weather_data = { "London": {"temperature": "15°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "80%"}, "New York": {"temperature": "20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": "50%"}, "Tokyo": {"temperature": "18°C", "conditions": "Rainy", "wind_speed": "7 km/h", "humidity": "90%"}, "Sydney": {"temperature": "22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity": "60%"}, "Paris": {"temperature": "17°C", "conditions": "Foggy", "wind_speed": "3 km/h", "humidity": "85%"} }

username = input("What's your name?")
print(f"Welcome {username}")

while True:
    city_name = input("Ask for the city name for which the weather forecast is needed: ")
    if city_name in weather_data:
        city_data = weather_data[city_name]
        print("\nWeather in " + city_name + ":")
        print("Temperature: " + weather_data[city_name]["temperature"])
        print("Condition: " + weather_data[city_name]["conditions"])
        print("Wind: " + weather_data[city_name]["wind_speed"])
        print("Humidity: " + weather_data[city_name]["humidity"])
        break
    else:
        print("City name not valid")


print("Thank ya, pal!")