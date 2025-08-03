import os
import tkinter as tk
from math import floor

from src.interface.layouts.Layout import Layout
from src.interface.widgets.Panel import Panel
from src.interface.widgets.Animation import Animation

MAX_PWR_OUTPUT = 80.0

class MainLayout(Layout):
    
    def __init__(self, parent: tk.Tk, width: int, height: int) -> None:
        Layout.__init__(self, parent, width, height)

    def __updatePanel__(self, panel: Panel) -> None:
        panel_id: str = panel.getID()
        content: int = self.car_data.getValue(panel_id)
        panel.updateContent(content)

    def __updateGif__(self, gif: Animation) -> None:
        num_frames: int = gif.getNumFrames()
        frame_index: int = floor(num_frames * self.car_data.getValue("PWR_OUTPUT") / MAX_PWR_OUTPUT)
        gif.setCurrentFrame(frame_index)

    def __setupWidgets__(self) -> None:
        for i in range(2): 
            self.canvas.grid_rowconfigure(i, weight=1)

        self.widgets["SOC"] = Panel(
            "SOC",
            self.canvas,
            self.width,
            self.height / 2,
            label="SOC [%]",
            content=0,
            content_size=80,
            outline="S",
            update_callback=self.__updatePanel__
        )
        self.widgets["PWR_OUTPUT"] = Panel(
            "PWR_OUTPUT",
            self.canvas,
            self.width / 3,
            self.height / 2,
            label="PWR OUTPUT [kW]",
            label_size=15,
            content=0,
            outline="E",
            update_callback=self.__updatePanel__
        )
        self.widgets["GIF"] = Animation(
            "GIF",
            self.canvas,
            self.width / 3,
            self.height / 2,
            os.getenv("ROOT_FOLDER") + "/assets/proton_logo.gif",
            outline="E",
            update_callback=self.__updateGif__
        )
        self.widgets["TEMP"] = Panel(
            "TEMP",
            self.canvas,
            self.width / 3,
            self.height / 2,
            label="CELL TEMP [°C]",
            label_size=15,
            content=0,
            update_callback=self.__updatePanel__
        )

        self.widgets["SOC"].grid(row=0, column=0, rowspan=1, columnspan=3)
        self.widgets["PWR_OUTPUT"].grid(row=1, column=0, rowspan=1, columnspan=1)
        self.widgets["GIF"].grid(row=1, column=1, rowspan=1, columnspan=1)
        self.widgets["TEMP"].grid(row=1, column=2, rowspan=1, columnspan=1)