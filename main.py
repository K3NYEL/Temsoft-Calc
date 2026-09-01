import tkinter as tk
import customtkinter as CTk

from backend.buttons.buttons import CustomButton
from backend.logic.buttons_logic import ButtonsLogic


class Application(tk.Tk):

    def __init__(self):
        super().__init__()

        # Ventana
        self.title("Calculator")
        self.geometry("320x500")
        self.resizable(False, False)

        CTk.set_appearance_mode("dark")

        self.main_frame = CTk.CTkFrame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.entry = CTk.CTkEntry(
            self.main_frame,
            height=60,
            font=("Roboto", 24),
            border_width=1,
            border_color="gray",
        )
        self.entry.pack(fill=tk.X, padx=5, pady=12)

        self.buttons_logic = ButtonsLogic(self.entry)

        self.buttons_frame = CTk.CTkFrame(
            self.main_frame, border_color="gray", border_width=1
        )
        self.buttons_frame.pack(padx=5, pady=5)

        self.footer_frame = CTk.CTkFrame(
            self.main_frame, height=40, border_color="gray", border_width=1
        )
        self.footer_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.label_footer = CTk.CTkLabel(
            self.footer_frame,
            text="Calculator by K3NYEL",
            font=("Roboto", 12),
        )
        self.label_footer.pack(pady=5)

        # Botones
        buttons = [
            "7",
            "8",
            "9",
            "/",
            "4",
            "5",
            "6",
            "*",
            "1",
            "2",
            "3",
            "-",
            ".",
            "0",
            "=",
            "+",
        ]

        for index, text in enumerate(buttons):

            row = index // 4
            column = index % 4

            if text == "=":
                command = self.buttons_logic.calculate
            else:
                command = lambda value=text: self.buttons_logic.add_to_entry(value)

            button = CustomButton(self.buttons_frame, text=text, command=command)

            button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")


if __name__ == "__main__":
    app = Application()
    app.mainloop()
