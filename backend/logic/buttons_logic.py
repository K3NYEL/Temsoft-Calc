import tkinter as tk
from colorama import Fore, Style, Back 

class ButtonsLogic:

    def __init__(self, entry):
        self.entry = entry
        print(Style.RESET_ALL + "\n" + Fore.GREEN + "ButtonsLogic initialized.", Style.RESET_ALL)  # Debug statement
        
    def add_to_entry(self, value):
        current_text = self.entry.get()
        new_text = current_text + str(value)

        self.entry.delete(0, tk.END)
        self.entry.insert(0, new_text)

        print(Style.RESET_ALL + Fore.BLUE + f"Number: [{value}]", Style.RESET_ALL)  # Debug statement
        print(Style.RESET_ALL + Fore.BLUE + f"Current entry: {new_text}", Style.RESET_ALL)  # Debug statement

    def clear_entry(self):
        self.entry.delete(0, tk.END)
        print(Style.RESET_ALL + Fore.RED + "Entry cleared.", Style.RESET_ALL)  # Debug statement

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)

            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
            print(Style.RESET_ALL + Fore.GREEN + f"Result: ['{expression}': '{result}']", Style.RESET_ALL)  # Debug statement

        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")