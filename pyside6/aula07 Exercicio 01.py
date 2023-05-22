from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QLabel
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exercicio 1")
        self.setFixedSize(QSize(300,200))

        self.inputA = QLineEdit()
        self.inputC = QLineEdit()
        self.inputL = QLineEdit()
        
        self.lbl = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.inputA)
        layout.addWidget(self.inputC)
        layout.addWidget(self.inputL)

        layout.addWidget(self.lbl)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)
        

app = QApplication(sys.argv)
w = MainWindow()
w.show()

app.exec()