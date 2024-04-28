import json
import os
import tkinter
from tkinter import messagebox
import requests
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime

import constants


class WeatherGui:

    def __init__(self):
        self.pictures_folder = os.path.join(os.getcwd(), "images")
        self.dict_images = {
            # to check if this is what the requests offer us
            "ClearDay": os.path.join(self.pictures_folder, "sunny.png"),
            "ClearNight": os.path.join(self.pictures_folder, "moon.png"),
            "Rain": os.path.join(self.pictures_folder, "rainy.png"),
            "Snow": os.path.join(self.pictures_folder, "snowy.png"),
            "Clouds": os.path.join(self.pictures_folder, "cloudy.png")
        }

    def get_weather(self, city_name):
        '''

        :param city_name: taken from the tkinter search
        :return: the degrees and the forecast
        '''

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={constants.API_KEY}"
        response = requests.get(url).content
        try:
            dictionary_response = json.loads(response.decode("utf-8"))
            ''' we need to get the temperature and the weather '''
            # 1. the conditions is in dictionary weather which contains a list of a single dictionary. The key is main
            conditions = dictionary_response["weather"][0]["main"]

            # 2 the temperature is in key main which is a dictionary and the key here is temp
            temperature = int(dictionary_response["main"]["temp"])
            print("Conditions: {}----Temperature: {}".format(conditions, temperature))
            return conditions, round(temperature, 2)
        except:
            messagebox.showerror("ORAS INVALID", "TE RUGAM INTRODU UN ORAS VALID")
            city_search_entry.delete(0, END)
            return

    def check_input(self):
        if city_search_entry.get():
            search_button["state"] = tkinter.NORMAL
        else:
            search_button["state"] = tkinter.DISABLED

    def split_label(self, text_label):
        return text_label.split(",")[0]

    def refresh_weather(self):
        global image
        city = self.split_label(label_city_selection["text"])
        # appeal the function to get weather
        weather_condition, temp = self.get_weather(city)
        date = datetime.now()
        hour = date.hour
        print(type(hour))
        # change the canvas based on the conditions
        if weather_condition == "Clear" and (5 < hour < 19):
            image = Image.open(self.dict_images["ClearDay"])
            image = ImageTk.PhotoImage(image.resize((220, 200)))
            canvas.itemconfig(init_image, image=image)
            string_label_city = city.capitalize() + ", " + str(temp) + "deg C " + ", " + weather_condition
            label_city_selection["text"] = string_label_city
            # clear search
            city_search_entry.delete(0, END)
            search_button["state"] = tkinter.DISABLED
        elif weather_condition == "Clear" and (hour > 19 or hour < 5):
            image = Image.open(self.dict_images["ClearNight"])
            image = ImageTk.PhotoImage(image.resize((220, 200)))
            canvas.itemconfig(init_image, image=image)
            string_label_city = city.capitalize() + ", " + str(temp) + "deg C " + ", " + weather_condition
            label_city_selection["text"] = string_label_city
            # clear search
            city_search_entry.delete(0, END)
            search_button["state"] = tkinter.DISABLED
        elif weather_condition == "Rain":
            image = Image.open(self.dict_images["Rain"])
            image = ImageTk.PhotoImage(image.resize((220, 200)))
            canvas.itemconfig(init_image, image=image)
            string_label_city = city.capitalize() + ", " + str(temp) + "deg C" + ", " + weather_condition
            label_city_selection["text"] = string_label_city
            # clear search
            city_search_entry.delete(0, END)
            search_button["state"] = tkinter.DISABLED
        elif weather_condition == "Snow":
            image = Image.open(self.dict_images["Snow"])
            image = ImageTk.PhotoImage(image.resize((220, 200)))
            canvas.itemconfig(init_image, image=image)
            string_label_city = city.capitalize() + ", " + str(temp) + "deg C" + ", " + weather_condition
            label_city_selection["text"] = string_label_city
            # clear search
            city_search_entry.delete(0, END)
            search_button["state"] = tkinter.DISABLED
        else:  # we will put cloudy for other thinks , fog etc
            image = Image.open(self.dict_images["Clouds"])
            image = ImageTk.PhotoImage(image.resize((220, 200)))
            canvas.itemconfig(init_image, image=image)
            string_label_city = city.capitalize() + ", " + str(temp) + "deg C" + ", " + weather_condition
            label_city_selection["text"] = string_label_city
            # clear search
            city_search_entry.delete(0, END)
            search_button["state"] = tkinter.DISABLED

    def get_actual_weather(self):
        global image
        city = city_search_entry.get()
        # appeal the function to get weather
        weather_condition, temp = self.get_weather(city)
        date = datetime.now()
        hour = date.hour
        # change the canvas based on the conditions
        if weather_condition == "Clear" and (5 < hour < 19):
            image = Image.open(self.dict_images["ClearDay"])
            image = ImageTk.PhotoImage(image.resize((220, 200)))
            canvas.itemconfig(init_image, image=image)
            string_label_city = city.capitalize() + ", " + str(temp) + "deg C " + ", " + weather_condition
            label_city_selection["text"] = string_label_city
            # clear search
            city_search_entry.delete(0, END)
            search_button["state"] = tkinter.DISABLED
            refresh_button["state"] = tkinter.NORMAL
        elif weather_condition == "Clear" and (hour > 19 or hour < 5):
            image = Image.open(self.dict_images["ClearNight"])
            image = ImageTk.PhotoImage(image.resize((220, 200)))
            canvas.itemconfig(init_image, image=image)
            string_label_city = city.capitalize() + ", " + str(temp) + "deg C " + ", " + weather_condition
            label_city_selection["text"] = string_label_city
            # clear search
            city_search_entry.delete(0, END)
            search_button["state"] = tkinter.DISABLED
            refresh_button["state"] = tkinter.NORMAL
        elif weather_condition == "Rain":
            image = Image.open(self.dict_images["Rain"])
            image = ImageTk.PhotoImage(image.resize((220, 200)))
            canvas.itemconfig(init_image, image=image)
            string_label_city = city.capitalize() + ", " + str(temp) + "deg C" + ", " + weather_condition
            label_city_selection["text"] = string_label_city
            # clear search
            city_search_entry.delete(0, END)
            search_button["state"] = tkinter.DISABLED
            # enable also the referesh button now as we have something on the screen
            refresh_button["state"] = tkinter.NORMAL
        elif weather_condition == "Snow":
            image = Image.open(self.dict_images["Snow"])
            image = ImageTk.PhotoImage(image.resize((220, 200)))
            canvas.itemconfig(init_image, image=image)
            string_label_city = city.capitalize() + ", " + str(temp) + "deg C" + ", " + weather_condition
            label_city_selection["text"] = string_label_city
            # clear search
            city_search_entry.delete(0, END)
            search_button["state"] = tkinter.DISABLED
            # enable also the referesh button now as we have something on the screen
            refresh_button["state"] = tkinter.NORMAL
        else:  # we will put cloudy for other thinks , fog etc
            image = Image.open(self.dict_images["Clouds"])
            image = ImageTk.PhotoImage(image.resize((220, 200)))
            canvas.itemconfig(init_image, image=image)
            string_label_city = city.capitalize() + ", " + str(temp) + "deg C" + ", " + weather_condition
            label_city_selection["text"] = string_label_city
            # clear search
            city_search_entry.delete(0, END)
            search_button["state"] = tkinter.DISABLED
            # enable also the referesh button now as we have something on the screen
            refresh_button["state"] = tkinter.NORMAL

    def build_gui(self):
        global app_menu
        global image_canvas
        global city_search_entry
        global label_city_selection
        global search_button, refresh_button
        global canvas
        global init_image
        app_menu = Tk()
        app_menu.title("Weather app")
        image_canvas = os.path.join(self.pictures_folder, "images.png")
        image_ico = os.path.join(self.pictures_folder, "weather.ico")
        app_menu.iconbitmap(image_ico)
        app_menu.geometry("300x275")
        app_menu.resizable(NO, NO)
        app_menu["bg"] = "#36EBCA"
        # create image
        image_canvas = PhotoImage(file=image_canvas)
        # create canvas
        canvas = Canvas(app_menu, height=200, width=450, bg="#36EBCA", bd=10, relief=tkinter.GROOVE)
        canvas.place(x=0, y=0)
        init_image = canvas.create_image((150, 75), image=image_canvas)
        # add entry and button
        label_city_search = Label(app_menu, text="CITY", justify="center",
                                  font=("Helvetica", 11, "bold"),
                                  cursor="star", fg="#2C143E", bg="#36EBCA")
        label_city_search.place(x=0, y=235)
        city_search_entry = Entry(app_menu, width=18, justify="center", font=("Helvetica", 9, "bold"),
                                  cursor="target",
                                  bg="#D4E2D0")
        city_search_entry.place(x=50, y=240)
        # put label which will tell us the city
        label_city_selection = Label(app_menu, text="", justify="left",
                                     font=("Helvetica", 13, "bold"),
                                     cursor="star", fg="#11311C", bg="#36EBCA")
        label_city_selection.place(x=20, y=180)
        # button
        search_button = Button(app_menu, text="SEARCH", width=13, height=1, fg="#1E2729", bg="#61A479",
                               font=("Helvetica", 9, "bold"),
                               command=self.get_actual_weather)
        search_button["state"] = tkinter.DISABLED
        refresh_button = Button(app_menu, text="REFRESH", width=13, height=1, fg="#1E2729", bg="#6896BC",
                                font=("Helvetica", 9, "bold"), command=self.refresh_weather)
        search_button["state"] = tkinter.DISABLED
        search_button.place(x=190, y=225)
        refresh_button["state"] = tkinter.DISABLED
        refresh_button.place(x=190, y=250)
        city_search_entry.bind("<KeyRelease>", lambda
            e: self.check_input())  # if a key is released check everytime if we have something written or not

        app_menu.mainloop()
