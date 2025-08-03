import tkinter as tk

class Widget(tk.Canvas):

    def __init__(
        self,
        id: str,
        parent: tk.Tk, 
        width: int, 
        height: int, 
        outline: str = ""
    ) -> None:
        tk.Canvas.__init__(self, parent, bg="black", width=width, height=height, highlightthickness=0)
        self.id: str = id
        self.width: int = width
        self.height: int = height
        self.update_callback: callable = None
        self.__createOutline__(outline)

    def __createOutline__(self, outline: str) -> None:
        if "W" in outline: self.create_line(0, 0, 0, self.height, width=2, fill="white")
        if "N" in outline: self.create_line(0, 0, self.width, 0, width=2, fill="white")
        if "E" in outline: self.create_line(self.width, 0, self.width, self.height, width=2, fill="white")
        if "S" in outline: self.create_line(0, self.height, self.width, self.height, width=2, fill="white")

    def getID(self) -> str:
        return self.id

    def update(self) -> None:
        if self.update_callback == None: return
        self.update_callback(self)