import tkinter as tk
from PIL import ImageTk,Image
import requests

# Static variables for the GUI

HEIGHT = 400
WIDTH = 400

def test_function(entry):
    print("This is the entry:", entry)

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# cffaccc932996bc116339849c4301e79

# Setting the Open Weather API

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        tempmin = weather['main']['temp_min']
        tempmax = weather['main']['temp_max']

        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s \nLowest (°C): %s \nHighest (°C): %s' % (name, desc, temp, tempmin, tempmax)
    except:
        final_str = 'This place has not yet been discovered'

    return final_str

# Connecting to the Open Weather API

def get_weather(city):
    weather_key = 'cffaccc932996bc116339849c4301e79'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

# root for GUI

root = tk.Tk()

# Canvas/Screen size

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

# Putting a bg image to the UI with PIL (Python Imaging Library)

bgimage = ImageTk.PhotoImage(Image.open("weather.jpg"))  # PIL solution
bglabel = tk.Label(root, image=bgimage)
bglabel.place(x=0,y=0,relwidth=1,relheight=1)

# frame for the entry and search button

frame = tk.Frame(root, bg="#dcf8c6", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

# Entry Box parameters

entry = tk.Entry(frame, font=50)
entry.place(relwidth=0.65,relheight=1)

# Button Parameters

button = tk.Button(frame, text="Get weather!", font=50, command=lambda: get_weather(entry.get()))
button.place(relx=0.675, relwidth=0.325,relheight=1)

# Lower Frame Param

lframe = tk.Frame(root, bg="#dcf8c6", bd=6.5)
lframe.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.65, anchor="n")

# Putting a label box in the lower frame

label = tk.Label(lframe, font=30)
label.place(relwidth=1,relheight=1)

root.mainloop()