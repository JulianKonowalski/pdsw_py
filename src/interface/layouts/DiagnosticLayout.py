import tkinter as tk

from src.interface.layouts.Layout import Layout
from src.interface.widgets.Table import Table

class DiagnosticLayout(Layout):

    def __init__(self, parent: tk.Tk, width: int, height: int) -> None:
        Layout.__init__(self, parent, width, height)

    def __updateTable__(self, table: Table):
        table.updateContent(self.car_data.getData())

    def __setupWidgets__(self):
        self.grid_rowconfigure(0, weight=1)
        self.widgets["TABLE"] = Table(
            "TABLE",
            self.canvas,
            self.width,
            self.height,
            content=self.car_data.getData(),
            update_callback=self.__updateTable__,
        )
        self.widgets["TABLE"].grid(row=0, column=0, rowspan=1, columnspan=1)
