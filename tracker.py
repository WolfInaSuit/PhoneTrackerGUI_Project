from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root = Tk()
root.title("Phone Number  Tracker")
root.geometry("365x584+300+200")
root.resizable(False, False)

# Icon image
icon = PhotoImage(file="tracker.png")
root.iconphoto(False, icon)

# Logo
logo = PhotoImage(file="tracker.png")
Label(root, image=logo).place(x=240, y=70)

Eback = PhotoImage(file="searchbar.png")
Label(root, image=Eback).place(x=20, y=115)

# Heading
Heading = Label(root, text="TRACK NUMBER", font=('arial', 15, 'bold'))
Heading.place(x=90, y=110)

# Bottom Box
# Box = PhotoImage(file='voice2.png') #
# Label(root, image=Box).place(x=-2, y=255) #








root.mainloop()
