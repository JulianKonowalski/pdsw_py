import tkinter as tk
from PIL import Image, ImageTk

from src.interface.widgets.Widget import Widget

class Animation(Widget):

    def __init__(
        self,
        id: str,
        parent: tk.Tk,
        width: int,
        height: int,
        gif_path: str,
        outline: str = "",
        update_callback: callable = None
    ) -> None:
        Widget.__init__(self, id, parent, width, height, outline)
        self.update_callback: callable = update_callback
        self.__loadGif__(gif_path)
        self.imageID: int = None
        self.setCurrentFrame(0)

    def __loadGif__(self, gif_path: str) -> None:
        gif: Image.ImageFile = Image.open(gif_path)
        self.frames: list[ImageTk.PhotoImage] = []
        while True:
            frame = gif.copy().resize((int(self.width), int(self.height)), Image.LANCZOS)
            self.frames.append(ImageTk.PhotoImage(master = self, image=frame))
            try: gif.seek(gif.tell() + 1)
            except EOFError: break

    def setCurrentFrame(self, frame_index: int) -> None:
        if frame_index < 0 or frame_index >= len(self.frames): return
        self.current_frame_index = frame_index
        if (self.imageID != None): self.delete(self.imageID)
        self.imageID = self.create_image(
            0, # x pos
            0, # y pos
            anchor="nw",
            image=self.frames[frame_index]
        )

    def getCurrentFrameIndex(self) -> int:
        return self.current_frame_index
    
    def getNumFrames(self) -> int:
        return len(self.frames)