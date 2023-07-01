import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('My App')

button1 = QPushButton("Click me 1")
button1.setStyleSheet("font-size: 30px; color: red; background-color: blue;")

button2 = QPushButton("Click me 2")
button2.setStyleSheet("font-size: 30px; color: red; background-color: blue;")

button3 = QPushButton("Click me 3")
button3.setStyleSheet("font-size: 30px; color: red; background-color: blue;")



layout = QGridLayout()
central_widget.setLayout(layout)
layout.addWidget(button1, 1, 1, 1, 1)
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 3, 1, 1, 2)

status_bar = window.statusBar()
status_bar.showMessage("Hello world!")

def slot_example(status_bar):
    status_bar.showMessage("O meu Slot foi executado")

menu = window.menuBar()
primeiro_menu = menu.addMenu("Primeiro menu")
primeira_acao = primeiro_menu.addAction("Primeira ação")
primeira_acao.triggered.connect(lambda: slot_example(status_bar))



window.show()

app.exec()