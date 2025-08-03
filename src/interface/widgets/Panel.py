import tkinter as tk

from src.interface.widgets.Widget import Widget

FONT_FAMILY = "Helvetica"

class Panel(Widget):

    def __init__(
        self,
        id: str,
        parent: tk.Tk,
        width: int, 
        height: int,
        label: str = "",
        label_size: int = 30,
        content: str = "",
        content_size: int = 60,
        outline: str = "",
        update_callback: callable = None
    ) -> None:
        Widget.__init__(self, id, parent, width, height, outline)
        self.update_callback: callable = update_callback
        self.labelID: int = self.create_text(
            self.width / 2, 
            label_size,
            fill="white", 
            text=label, 
            font=(FONT_FAMILY, label_size)
        )
        self.contentID: int = self.create_text(
            self.width / 2, 
            self.height / 2, 
            fill="white", 
            text=content, 
            font=(FONT_FAMILY, content_size)
        )
    
    def updateContent(self, content: int) -> None:
        self.itemconfigure(self.contentID, text=f"{content}")