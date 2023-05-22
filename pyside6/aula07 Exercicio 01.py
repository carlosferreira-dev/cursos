from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QLabel
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exercicio 1")
        self.setFixedSize(QSize(300,200))

        self.txt_Altura = QLineEdit()
        self.txt_Comprimento = QLineEdit()
        self.txt_Largura = QLineEdit()
        
        self.lbl = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.txt_Altura)
        layout.addWidget(self.txt_Comprimento)
        layout.addWidget(self.txt_Largura)

        layout.addWidget(self.lbl)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)
        

app = QApplication(sys.argv)
w = MainWindow()
w.show()

app.exec()