from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('Basic Calculator')
        self.setGeometry(100, 100, 300, 400)

        grid = QGridLayout()
        self.setLayout(grid)
        
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFont(QFont('Arial', 24))
        grid.addWidget(self.display, 0, 0, 1, 4)

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
            button_widget = QPushButton(text)
            button_widget.setFont(QFont('Arial', 18))
            button_widget.clicked.connect(lambda _, t=text: self.on_button_click(t))
            grid.addWidget(button_widget, row, col, 1, colspan)
        
    def on_button_click(self, text):
        if text == 'C':
            self.display.clear()
        elif text == '=':
            try:
                expression = self.display.text()
                result = str(eval(expression))
                self.display.setText(result)
            except Exception:
                self.display.setText('Error')
        else:
            current_text = self.display.text()
            new_text = current_text + text
            self.display.setText(new_text)

if __name__ == '__main__':
    app = QApplication([])
    calc = CalculatorApp()
    calc.show()
    app.exec_()
