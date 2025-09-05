import tkinter as tk
from tkinter import ttk


class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")
        self.geometry("500x600")
        self.minsize(500, 600)
        #maxsize(1000, 1200)
        self.mainloop()
