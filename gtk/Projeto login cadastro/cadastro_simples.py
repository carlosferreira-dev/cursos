# coding-utf-8
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class User():
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

class Handler(object):
    def __init__(self):
        self.modelo_armazenamento: Gtk.ListStore = Builder.get_object("liststore1")
        self.Stack: Gtk.Stack = Builder.get_object("stack")
        self.banco_dados = []

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
            self.Stack.set_visible_child_name('view_inicial')
            window.props.title = 'Bem-vindo'
            window.props.icon_name = 'avatar-default'
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

    def on_button_cadastrar_inicial_clicked(self, button):
        self.Stack.set_visible_child_name('view_cadastro')
    
    def on_button_cad_voltar_clicked(self, button):
        self.Stack.set_visible_child_name('view_inicial')

    def on_button_cad_cadastrar_clicked(self, button):
        nome = Builder.get_object("cad_nome").get_text()
        email = Builder.get_object("cad_email").get_text()
        if nome == '':
            self.mensagem('Aviso', 'O campo nome é obrigatório!', 'dialog-error')
        else:
            self.banco_dados.append(User(len(self.banco_dados)+1, nome, email))
            self.mensagem('Aviso', 'Usuário cadastrado com sucesso!', 'emblem-default')
            nome = Builder.get_object("cad_nome").set_text('')
            email = Builder.get_object("cad_email").set_text('')

    def on_button_listar_inicial_clicked(self, button):
        self.Stack.set_visible_child_name('view_listar')

    def on_button_listar_voltar_clicked(self, button):
        self.Stack.set_visible_child_name('view_inicial')

    def on_button_listar_clicked(self, button):
        self.modelo_armazenamento.clear()
        for user in self.banco_dados:
            self.modelo_armazenamento.append((user.id, user.nome, user.email))

    def on_button_sair_inicial_clicked(self, button):
        self.Stack.set_visible_child_name('view_login')
        window.props.icon_name = 'changes-prevent'

Builder = Gtk.Builder()
Builder.add_from_file("user_interface.glade")
Builder.connect_signals(Handler())
window: Gtk.Window = Builder.get_object("main_window") 
window.show_all()
Gtk.main()
