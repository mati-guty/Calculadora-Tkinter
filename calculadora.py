import tkinter as tk
from math import *


class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_ui()

    def create_ui(self):
        # Pantalla
        result_label = tk.Label(
            self.root, textvariable=self.result_var, font=("Arial", 24), anchor="e")
        result_label.grid(row=0, column=0, columnspan=6)

        # Botones
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("^2", 5, 3),
            ("sqrt", 6, 0), ("log", 6, 1), ("exp", 6, 2), ("(", 6, 3),
            (")", 7, 0), ("pi", 7, 1), ("e", 7, 2), ("Clear", 7, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=(
                "Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, button_text):
        current_result = self.result_var.get()

        if button_text == "=":
            try:
                result = str(eval(current_result))
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        elif button_text == "Clear":
            self.result_var.set("0")
        else:
            if current_result == "0" or current_result == "Error":
                self.result_var.set(button_text)
            else:
                self.result_var.set(current_result + button_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
