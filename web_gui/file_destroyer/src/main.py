from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path


def main():

    def open_files():
        file_names, _ = QFileDialog.getOpenFileNames(window,'Select Files')
        print(file_names, "file names")

        for filename in file_names:
            path = Path(filename)
            with open(path, "wb") as file:
                file.write(b'')
            path.unlink()
            print(f"Deleted {path}")
               



    app = QApplication([])
    window = QWidget() 
    window.setWindowTitle("File Destroyer")
    layout = QVBoxLayout()


    description = QLabel("This application securely deletes files by overwriting them multiple times before deletion.")
    layout.addWidget(description)

    open_btn= QPushButton("Open File")
    open_btn.setToolTip("Open a file to securely delete it")
    open_btn.setFixedWidth(100)
    layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    open_btn.clicked.connect(open_files )

    window.setLayout(layout)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()