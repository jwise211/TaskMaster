from gi.repository import Gtk

class MainWin(Gtk.Window):
    
    def __init__(self):
        
        Gtk.Window.__init__(self, title="Task Master")
        self.connect("delete-event", Gtk.main_quit)
    

win = MainWin()
win.show_all()
Gtk.main()