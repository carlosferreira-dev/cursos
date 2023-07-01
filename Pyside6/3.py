import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

app = QApplication(sys.argv)

button = QPushButton("Click me")
button.setStyleSheet("font-size: 30px; color: red; background-color: blue;")

button2 = QPushButton("Click me 2")
button2.setStyleSheet("font-size: 30px; color: red; background-color: blue;")

button3 = QPushButton("Click me 3")
button3.setStyleSheet("font-size: 30px; color: red; background-color: blue;")

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)
layout.addWidget(button, 1, 1, 1, 1)
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 3, 1, 1, 2)

central_widget.show()

app.exec()