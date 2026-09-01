import tkinter as tk
from colorama import Fore, Style


class ButtonsLogic:

    def __init__(self, entry):
        self.entry = entry
        self.ascii_art()

    def ascii_art(self):
        art = r""" _____                              __  _                 _       
|_   _|___  _ __ ___   ___   ___   / _|| |_    ___  __ _ | |  ___ 
  | | / _ \| '_ ` _ \ / __| / _ \ | |_ | __|  / __|/ _` || | / __|
  | ||  __/| | | | | |\__ \| (_) ||  _|| |_  | (__| (_| || || (__ 
  |_| \___||_| |_| |_||___/ \___/ |_|   \__|  \___|\__,_||_| \___|"""
        print(Style.RESET_ALL + Fore.CYAN + art, Style.RESET_ALL)  # Debug statement
        print(
            Style.RESET_ALL + "\n" + Fore.GREEN + "ButtonsLogic initialized.",
            Style.RESET_ALL, "\n"
        )  # Debug statement

    def add_to_entry(self, value):
        current_text = self.entry.get()
        new_text = current_text + str(value)

        self.entry.delete(0, tk.END)
        self.entry.insert(0, new_text)

        print(
            "\n", Style.RESET_ALL + Fore.BLUE + f"Number: [{value}]", Style.RESET_ALL
        )  # Debug statement
        print(
            Style.RESET_ALL + Fore.BLUE + f"Current entry: {new_text}", Style.RESET_ALL, "\n"
        )  # Debug statement

    def clear_entry(self):
        self.entry.delete(0, tk.END)
        print(
            Style.RESET_ALL + Fore.RED + "Entry cleared.", Style.RESET_ALL
        )  # Debug statement

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)

            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
            print(
                Style.RESET_ALL + Fore.GREEN + f"Result: ['{expression}': '{result}']",
                Style.RESET_ALL,
            )  # Debug statement

        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")
            print(
                Style.RESET_ALL + Fore.RED + "Error in calculation.", Style.RESET_ALL
            )  # Debug statement
