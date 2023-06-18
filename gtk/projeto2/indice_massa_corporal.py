import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file('C:/GitHub/cursos/gtk/projeto2/user_interface.glade')


class Handler():
    def __init__(self):
        self.peso = builder.get_object('peso')
        self.altura = builder.get_object('altura')
        self.text_buffer = builder.get_object('textbuffer1')

    def on_button1_clicked(self, button1):
        imc = float(self.peso.get_text()) / (float(self.altura.get_text().replace(',', '.')) ** 2)
        self.text_buffer.set_text("Seu IMC é: " + str(round(imc, 2)))

    def on_main_window_destroy(self, window):
        Gtk.main_quit()


builder.connect_signals(Handler())
window = builder.get_object('main_window')
window.show_all()
Gtk.main()
