import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")
        self.root.geometry("300x400")
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self.root, font=("Arial", 24), bd=10, insertwidth=4, width=14, borderwidth=4, justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0, 4)
        ]

        for button in buttons:
            text = button[0]
            row = button[1]
            col = button[2]
            colspan = button[3] if len(button) > 3 else 1
            tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 18), command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, columnspan=colspan, sticky='nsew')

        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        if button_text == 'C':
            self.display.delete(0, tk.END)
        elif button_text == '=':
            try:
                expression = self.display.get()
                result = str(eval(expression))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            current_text = self.display.get()
            new_text = current_text + button_text
            self.display.delete(0, tk.END)
            self.display.insert(0, new_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
