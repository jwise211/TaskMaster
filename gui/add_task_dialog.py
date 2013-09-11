from gi.repository import Gtk

class AddTaskDialog(Gtk.Dialog):
    
    def __init__(self, parent_win):
        
        Gtk.Dialog.__init__(self, title="Add Task...", parent=parent_win)
        self.main_box = Gtk.Box().set_orientation(Gtk.Orientation.Vertical)
        
        