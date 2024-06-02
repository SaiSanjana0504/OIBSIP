import requests
def get_weather(api_key, location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
        temp_index = data.find('"temp":') + len('"temp":')
        temp_end_index = data.find(',', temp_index)
        temperature = data[temp_index:temp_end_index]
        humidity_index = data.find('"humidity":') + len('"humidity":')
        humidity_end_index = data.find(',', humidity_index)
        humidity = data[humidity_index:humidity_end_index]
        description_index = data.find('"description":"') + len('"description":"')
        description_end_index = data.find('"', description_index)
        description = data[description_index:description_end_index]
        city_index = data.find('"name":"') + len('"name":"')
        city_end_index = data.find('"', city_index)
        city = data[city_index:city_end_index]
        print(f'Weather in {city}:')
        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
        print(f'Conditions: {description}')
    else:
        print('Failed to retrieve weather data.')
api_key = '648dc500234781deeacada87bb99eb6d'
location = input("enter city:")
get_weather(api_key, location)