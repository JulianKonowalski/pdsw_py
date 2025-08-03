import tkinter as tk
from math import floor

from src.interface.widgets.Widget import Widget

FONT_FAMILY: str = "Helvetica"

class TableRow(Widget):

    def __init__(
        self,
        id: str,
        parent: tk.Tk,
        width: int,
        height: int,
        label: str,
        content: str,
        font_size: int = 10,
        outline: str = ""
    ) -> None:
        Widget.__init__(self, id, parent, width, height, outline)
        self.font_size: int = font_size
        self.__createLabel__(label)
        self.__createContent__(content)

    def __createLabel__(self, label: str) -> None:
        self.label_id: int = self.create_text(
            0, # placeholder x pos
            0, # placeholder y pos
            fill="white",
            text=label,
            font=(FONT_FAMILY, self.font_size)
        )
        label_coords: tuple[int, int, int, int] = self.bbox(self.label_id)
        label_x_offset: int = self.font_size + floor((label_coords[2] - label_coords[0]) / 2)
        self.move(self.label_id, label_x_offset, self.height / 2)


    def __createContent__(self, content: str) -> None:
        self.content_id: int = self.create_text(
            0, # placeholder x pos
            0, # placeholder y pos
            fill="white",
            text=content,
            font=(FONT_FAMILY, self.font_size)
        )
        content_coords: tuple[int, int, int, int] = self.bbox(self.content_id)
        content_x_offset: int = ((self.width - content_coords[2] + content_coords[0]) / 2) - self.font_size
        self.move(self.content_id, content_x_offset, self.height / 2) 

    def updateLabel(self, label: str) -> None:
        self.itemconfigure(self.label_id, text=f"{label}")

    def updateContent(self, content: int) -> None:
        self.itemconfigure(self.content_id, text=f"{content}")


class Table(Widget):

    def __init__(
        self,
        id: str,
        parent: tk.Tk, 
        width: int, 
        height: int, 
        content: dict,
        outline: str = "",
        update_callback: callable = None
    ) -> None:
        Widget.__init__(self, id, parent, width, height, outline)
        self.update_callback: callable = update_callback
        font_size: int = floor(self.height / (2 * len(content))) - 5
        self.__setupRows__(content, font_size)

    def __setupRows__(self, content: dict, font_size: int) -> None:
        self.rows: dict = {}
        for index, key in enumerate(content):
            self.rows[key] = TableRow(
                key, 
                self,
                self.width,
                floor(self.height / len(content)),
                key,
                content[key],
                font_size=font_size
            )
            self.rows[key].grid(row=index, column=0)
    
    def updateContent(self, content: dict) -> None:
        self.content: dict = content        
        for row_key in self.rows:
            self.rows[row_key].updateContent(f"{self.content[row_key]}")