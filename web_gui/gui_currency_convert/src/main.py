from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit



def main():
    def make_sentences():
        input_text = text.text()
        output_label.setText(f"You entered: {input_text}")

    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Sentence Maker")

    layout = QVBoxLayout()

    label = QLabel("Enter a sentence:")
    layout.addWidget(label)
   
   
    text = QLineEdit()
    layout.addWidget(text)

    btn = QPushButton('Submit')
    layout.addWidget(btn)

    btn.clicked.connect(make_sentences)
    
    output_label = QLabel("")
    layout.addWidget(output_label)

    window.setLayout(layout)



    window.show()
    app.exec()


if __name__ == "__main__":
    main()