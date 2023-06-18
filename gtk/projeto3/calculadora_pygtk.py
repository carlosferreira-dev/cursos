import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from calculadora import Calculadora

builder = Gtk.Builder()
builder.add_from_file("user_interface.glade")

class Handler(object):
    def __init__(self):
        self.usar_estilo()
        self.display = builder.get_object("display")
        self.display.set_text("0")
        self.primeiro_numero = None
        self.operacao = None
        self.calculadora = Calculadora()
        self.limpar_display = None

    def usar_estilo(self):
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('static/css/style.css')
        screen = Gdk.Screen.get_default()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def on_main_window_destroy(self, window):
        Gtk.main_quit()

    def on_botao_clicked(self, botao):
        if self.limpar_display:
            self.display.set_text("0")
            self.limpar_display = False

        if self.display.get_text() == "0":
            self.display.set_text(str(botao.get_label()))
        else:
            self.display.set_text(str(self.display.get_text() + botao.get_label()))
    
    def on_botao_ponto_clicked(self, botao_ponto):
        self.display.set_text(str(self.display.get_text() + botao_ponto.get_label()))

    def on_botao_reset_clicked(self, botao_reset):
        self.display.set_text("0")
    
    def ler_display(self):
        string = self.display.get_text()
        try:
            numero = int(string)
        except:
            numero = float(string)
        return numero

    def on_botao_igual_clicked(self, botao_igual):
        numero_atual = self.ler_display()
        resultado = self.calculadora.funcoes[self.operacao](self.primeiro_numero, numero_atual)
        self.display.set_text(str(resultado))
        self.limpar_display = True

    def on_botao_soma_clicked(self, botao_soma):
        self.primeiro_numero = self.ler_display()
        self.operacao = "soma"
        self.limpar_display = True    

    def on_botao_subtracao_clicked(self, botao_subtracao):
        self.primeiro_numero = self.ler_display()
        self.operacao = "subtracao"
        self.limpar_display = True
    
    def on_botao_multiplicacao_clicked(self, botao_multiplicacao):
        self.primeiro_numero = self.ler_display()
        self.operacao = "multiplicacao"
        self.limpar_display = True
    
    def on_botao_divisao_clicked(self, botao_divisao):
        self.primeiro_numero = self.ler_display()
        self.operacao = "divisao"
        self.limpar_display = True

    def on_botao_porcentagem_clicked(self, botao_porcentagem):
        self.primeiro_numero = self.ler_display()
        self.operacao = "porcentagem"
        self.limpar_display = True

    def on_botao_raiz_quadrada_clicked(self, botao_raiz_quadrada):
        numero_atual = self.ler_display()
        resultado = self.calculadora.funcoes["raiz_quadrada"](numero_atual)
        self.display.set_text(str(resultado))

builder.connect_signals(Handler())
window = builder.get_object("main_window")
window.show_all()
Gtk.main()