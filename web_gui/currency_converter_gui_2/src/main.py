from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit

from utils.currency_exchange_rate import get_currency



def main():
    def show_currency():
        input_text = text.text()
        result = get_currency(float(input_text))
        output_label.setText(str(result) + '.')

    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Currency Converter")

    layout = QVBoxLayout()
    label = QLabel("Enter amount (USD): ")
    layout.addWidget(label)
   
   
    text = QLineEdit()
    layout.addWidget(text)

    btn = QPushButton('Converter to EUR')
    layout.addWidget(btn)

    btn.clicked.connect(show_currency)
    
    output_label = QLabel("")
    layout.addWidget(output_label)

    window.setLayout(layout)



    window.show()
    app.exec()


if __name__ == "__main__":
    main()