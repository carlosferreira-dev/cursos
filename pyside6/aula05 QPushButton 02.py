from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meu primeiro programa")
        self.setFixedSize(QSize(600,400))

        self.button = QPushButton("Botão")
        self.setCentralWidget(self.button)

        self.button.setCheckable(True)
        self.button.clicked.connect(self.imprimir)
        self.button.clicked.connect(self.clicado)

    def imprimir(self):
        print("testando botão")

    def clicado(self, s):
        print("LIGADO:", s)
        if s:
            self.button.setStyleSheet(u"background-color:green")
            self.button.setText("LIGADO!")
        else:
            self.button.setStyleSheet(u"background-color:red")
            self.button.setText("DESLIGADO!")
        
        self.button.setEnabled(False)
        

app = QApplication(sys.argv)
w = MainWindow()
w.show()

app.exec()