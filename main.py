from tkinter import *
from PIL import ImageTk,Image
import requests

url = "https://api.openweathermap.org/data/2.5/weather"
api_key = "f34be76f5a61668061f4573d57665d7d"
resim_icon = "https://openweathermap.org/img/wn/{}@2x.png"

def havaDurumu(city):
    parametre = { "q" :city, "appid" : api_key, "lang": "tr" }
    veri = requests.get(url,params=parametre).json()
    if veri:
        city = veri["name"].capitalize()
        ulke = veri["sys"]["country"]
        sicak = int(veri["main"]["temp"] - 273.15)
        icon = veri["weather"][0]["icon"]
        durum = veri["weather"][0]["description"]
        return (city,ulke,sicak,icon,durum)

def menu():
    city = sehir_Onay.get()
    weather = havaDurumu(city)
    if weather:
        yer['text'] = "{},{}".format(weather[0], weather[1])
        sıcaklık['text'] = "{}°C".format(weather[2])
        toplu['text'] = weather[4]
        icon = ImageTk.PhotoImage(Image.open(requests.get(resim_icon.format(weather[3]),stream=True).raw))
        iconL.configure(image=icon)


ekran = Tk()
ekran.geometry("400x450")
ekran.title("Hava Durumu")

sehir_Onay = Entry(ekran,justify="center")
sehir_Onay.pack(fill=BOTH, ipady=10,padx=18, pady=5)
sehir_Onay.focus()

buton = Button(ekran, text="Hava Durumu",font=("Arial",12),command=menu)
buton.pack(fill=BOTH, ipady=10,padx=15)

iconL = Label(ekran)
iconL.pack()

yer = Label(ekran,font=("Arial",35))
yer.pack()

sıcaklık = Label(ekran,font=("Arial",50,"bold"))
sıcaklık.pack()

toplu = Label(ekran,font=("Arial",20))
toplu.pack()

ekran.mainloop()