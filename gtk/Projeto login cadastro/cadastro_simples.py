# coding-utf-8
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler(object):
    def __init__(self):
        pass

    def on_main_window_destroy(self, window):
        Gtk.main_quit()

    def on_button_login_clicked(self, button):
        email = Builder.get_object("email").get_text()
        senha = Builder.get_object("senha").get_text()
        lembrar = Builder.get_object("lembrar").get_active()
        self.login(email, senha, lembrar)

    def login(self, email, senha, lembrar):
        if email == 'admin' and senha == 'admin':
            self.mensagem('Bem-vindo', 'Usuário logado com sucesso!', 'emblem-default')
        else:
            self.mensagem('Aviso', 'Email ou senha incorretos!', 'dialog-error')

    def mensagem(self, titulo, msg, icone):
        mensagem: Gtk.MessageDialog = Builder.get_object("mensagem")
        mensagem.props.text = titulo
        mensagem.props.secondary_text = msg
        mensagem.props.icon_name = icone
        mensagem.show_all()
        mensagem.run()
        mensagem.hide()

Builder = Gtk.Builder()
Builder.add_from_file("user_interface.glade")
Builder.connect_signals(Handler())
window: Gtk.Window = Builder.get_object("main_window") 
window.show_all()
Gtk.main()
