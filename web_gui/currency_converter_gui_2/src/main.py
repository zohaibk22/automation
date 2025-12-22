from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox

from utils.currency_exchange_rate import get_currency



def main():
    def show_currency():
        input_text = text.text()
        input_currency = in_combo.currentText()
        target_currency = target_combo.currentText()
        result = get_currency(float(input_text), from_currency=input_currency, to_currency=target_currency)
        output_label.setText(f"{input_text} {input_currency} is {result} {target_currency}.")

    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Currency Converter")

    layout = QVBoxLayout()
    label = QLabel("Enter amount (USD): ")
    layout.addWidget(label)

    in_combo = QComboBox()
    currencies = ['USD', 'GBP', 'CAD', 'AUD', 'INR']
    in_combo.addItems(currencies)
    layout.addWidget(in_combo)

    target_combo = QComboBox()
    currencies = ['USD', 'GBP', 'CAD', 'AUD', 'INR']
    target_combo.addItems(currencies)
    layout.addWidget(target_combo)
   
   
   
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