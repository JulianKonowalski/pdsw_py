import tkinter as tk

from src.interface.widgets.Panel import Panel
from src.spi.CarData import CarData

DEMO_LABEL: str   = "Demo"
DEMO_CONTENT: str = "This is a demo layout.\nTo customize it override the\nLayout::__setupWidgets__ method."

class Layout(tk.Frame):

    def __init__(self, parent: tk.Tk, width: int, height: int) -> None:
        tk.Frame.__init__(self, parent)
        self.width: int = width
        self.height: int = height

        self.widgets: dict = {}
        self.car_data: CarData = CarData()

        self.__setupCanvas__()
        self.__setupWidgets__()

    def __setupCanvas__(self) -> None:
        self.canvas: tk.Canvas = tk.Canvas(
            self,
            bg="black",
            height=self.height,
            width=self.width            
        )
        self.canvas.grid(row=0, column=0)

    def __setupWidgets__(self) -> None:
        self.widgets["DEMO"] = Panel(
            "DEMO",
            self.canvas,
            self.width, 
            self.height, 
            label=DEMO_LABEL,
            content=DEMO_CONTENT,
            content_size=30,
            outline="NESW"
        )
        self.widgets["DEMO"].grid(row=0, column=0)

    def update(self, car_data: CarData) -> None:
        self.car_data: CarData = car_data
        for widget_key in self.widgets:
            self.widgets[widget_key].update()