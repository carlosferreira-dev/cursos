from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        self.setCentralWidget(button)
        button.clicked.connect(self.printer)

    def printer(self):
        print("Button clicked, Hello!")
    
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()