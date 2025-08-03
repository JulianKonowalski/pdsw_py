import tkinter as tk

FONT_FAMILY = "Helvetica"

class Popup(tk.Frame):

    def __init__(
        self, 
        parent: tk.Tk,
        message: str,
        message_size: int = 60,
        duration_ms: int = 750
    ) -> None:
        tk.Frame.__init__(self, parent, bg="black")
        self.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        border: tk.Frame = tk.Frame(self, bg="white", padx=10, pady=10)
        border.pack(expand=True, fill="both")

        inner_frame: tk.Frame = tk.Frame(border, bg="black")
        inner_frame.pack(expand=True, fill="both")
        
        label: tk.Label = tk.Label(
            inner_frame, 
            text=message,
            fg="white",
            bg="black",
            font=(FONT_FAMILY, message_size)
        )
        label.pack(expand=True)

        self.after(duration_ms, self.destroy)