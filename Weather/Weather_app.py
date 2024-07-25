from tkinter import *
from configparser import ConfigParser
import requests
from PIL import Image, ImageTk
from io import BytesIO

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json_data = result.json()
        city = json_data['name']
        country = json_data['sys']['country']
        temp_kelvin = json_data['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        weather = json_data['weather'][0]['description']
        icon = json_data['weather'][0]['icon']
        final = (city, country, temp_celsius, weather, icon)
        return final
    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        temp_lbl['text'] = '{:.2f}°C'.format(weather[2])
        weather_lbl['text'] = weather[3]

        # Update weather icon
        icon_code = weather[4]
        icon_url = f'http://openweathermap.org/img/wn/{icon_code}@2x.png'
        icon_response = requests.get(icon_url)
        icon_data = icon_response.content
        icon_image = Image.open(BytesIO(icon_data))
        icon_photo = ImageTk.PhotoImage(icon_image)
        image.config(image=icon_photo)
        image.image = icon_photo  # Keep a reference to avoid garbage collection
    else:
        location_lbl['text'] = 'City not found'
        temp_lbl['text'] = ''
        weather_lbl['text'] = ''
        image.config(image='')


app = Tk()
app.title("Weather app")
app.geometry('700x350')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text='Search Weather', width=12, command=search)
search_btn.pack()

location_lbl = Label(app, text='', font=('bold', 20))
location_lbl.pack()

temp_lbl = Label(app, text='')
temp_lbl.pack()

weather_lbl = Label(app, text='')
weather_lbl.pack()

image = Label(app, bitmap='')
image.pack()

app.mainloop()

