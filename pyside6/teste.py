from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication, QScreen, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Definir o título da janela
        self.setWindowTitle("Exemplo de Janela Full Screen")

        # Criar um layout vertical para organizar os botões
        layout = QVBoxLayout()

        # Criar botões de exemplo com ícones
        push_button = QPushButton(QIcon.fromTheme("document-save"), "Salvar")
        toggle_button = QPushButton(QIcon.fromTheme("media-playback-start"), "Iniciar")
        radio_button = QPushButton(QIcon.fromTheme("dialog-info"), "Informação")
        check_box = QPushButton(QIcon.fromTheme("dialog-warning"), "Aviso")
        flat_button = QPushButton(QIcon.fromTheme("edit-cut"), "Recortar")
        menu_button = QPushButton(QIcon.fromTheme("application-menu"), "Menu")
        tool_button = QPushButton(QIcon.fromTheme("preferences-system"), "Configurações")

        # Adicionar os botões ao layout
        layout.addWidget(push_button)
        layout.addWidget(toggle_button)
        layout.addWidget(radio_button)
        layout.addWidget(check_box)
        layout.addWidget(flat_button)
        layout.addWidget(menu_button)
        layout.addWidget(tool_button)

        # Criar um widget central para a janela e definir o layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Definir a janela para ser exibida em tela cheia
        self.setWindowState(Qt.WindowFullScreen)


if __name__ == "__main__":
    # Criação da instância do aplicativo Qt
    app = QApplication([])

    # Obter a resolução da tela primária
    screen = QGuiApplication.primaryScreen()
    screen_resolution = screen.availableGeometry()

    # Criação da instância da janela principal
    window = MainWindow()

    # Definir o tamanho da janela para a resolução da tela
    window.resize(screen_resolution.width(), screen_resolution.height())

    # Exibir a janela em tela cheia
    window.showFullScreen()

    # Executar o loop principal do aplicativo
    app.exec()
