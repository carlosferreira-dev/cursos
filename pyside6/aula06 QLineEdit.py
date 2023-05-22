from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QLabel
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QlineEdit")
        #self.setFixedSize(QSize(300,200))

        self.input = QLineEdit()
        self.lbl = QLabel()
        
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.lbl)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.input.textChanged.connect(self.texto)



    def texto(self):
        self.lbl.setText("Valor alterado")
        

app = QApplication(sys.argv)
w = MainWindow()
w.show()

app.exec()