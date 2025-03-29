from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys
from PyQt6.QtCore import QSize, Qt

# app = QApplication(sys.argv) # for passing cmd arguments
 # without cmd arguments
# window = QWidget()
# window = QPushButton("Push Me")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        # Set the central widget of the Window.
        self.setCentralWidget(button)

app = QApplication([])
window = MainWindow()
window.show()

app.exec()