import customtkinter as ctk

class CustomButton(ctk.CTkButton):

    def __init__(self, master, text, command=None):
        super().__init__(
            master,
            text=text,
            width=67,
            height=70,
            font=("Roboto", 24),
            corner_radius=10,
            fg_color="gray",
            border_color="gray",
            hover_color="red",
            command=command
        )