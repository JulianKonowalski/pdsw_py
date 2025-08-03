import tkinter as tk
from tkinter import ttk

from src.spi.CarData import CarData
from src.interface.widgets.Popup import Popup
from src.interface.layouts.Layout import Layout
from src.interface.layouts.MainLayout import MainLayout
from src.interface.layouts.DiagnosticLayout import DiagnosticLayout 

WIDTH: int          = 800
HEIGHT: int         = 440
IS_FULLSCREEN: bool = False 
WINDOW_TITLE: str   = "PD_SW_INTERFACE"

class Interface(tk.Tk):

    def __init__(self) -> None:
        tk.Tk.__init__(self)
        self.__setupWindow__()
        self.__setupLayouts__()
        self.car_data: CarData = CarData()
        self.soc_state: int = None
    
    def __setupWindow__(self) -> None:
        self.title(WINDOW_TITLE)
        self.attributes("-fullscreen", IS_FULLSCREEN)
        self.container: ttk.Frame = ttk.Frame(self)
        self.container.pack(side="top", fill="both", expand=False)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def __setupLayouts__(self) -> None:
        self.layouts: list[Layout] = []
        self.layouts.append(MainLayout(self.container, WIDTH, HEIGHT))
        self.layouts.append(DiagnosticLayout(self.container, WIDTH, HEIGHT))
        for layout in self.layouts: layout.grid(row=0, column=0)
    
    def __redraw__(self) -> None:
        for layout in self.layouts:
            layout.update(self.car_data)

    def __update__(self) -> None:
        self.update_callback()
        self.__redraw__()
        self.after(1, self.__update__)

    def run(self, update_callback: callable) -> None:
        self.update_callback: callable = update_callback
        self.current_layout = 0
        self.layouts[self.current_layout].tkraise()
        self.__update__()
        self.mainloop()

    def nextScreen(self) -> None:
        if self.current_layout >= len(self.layouts) - 1: return
        self.current_layout += 1
        self.layouts[self.current_layout].tkraise()

    def previousScreen(self) -> None:
        if self.current_layout <= 0: return
        self.current_layout -= 1
        self.layouts[self.current_layout].tkraise()

    def setCarData(self, car_data: CarData) -> None:
        self.car_data: CarData = car_data 

    def tickSocDeltaTimer(self) -> None:
        if self.soc_state == None: Popup(self, "Started SOC delta")
        else: Popup(self, f"Delta: {self.soc_state - self.car_data.getValue("SOC")}")
        self.soc_state = self.car_data.getValue("SOC")