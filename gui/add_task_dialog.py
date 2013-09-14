from gi.repository import Gtk

class AddTaskDialog(Gtk.Dialog):
    
    def __init__(self, parent_win):
        
        Gtk.Dialog.__init__(self, title="Add Task...", parent=parent_win)
        self.parent = parent_win
        self.main_box = self.get_content_area()
        self.main_box.set_orientation(Gtk.Orientation.VERTICAL)
        
        self.txt_box = Gtk.Box()
        self.txt_box.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.task_lbl = Gtk.Label("Task Description:")
        self.task_desc = Gtk.TextView()
        self.task_desc.set_editable(True)
        self.txt_box.pack_start(self.task_lbl, True, False, 0)
        self.txt_box.pack_start(self.task_desc, True, False, 0)
        self.main_box.pack_start(self.txt_box, True, False, 0)
        
        self.txt_box.show()
        self.task_lbl.show()
        self.task_desc.show()
        
        self.add_but = Gtk.Button("_Add", use_underline=True)
        self.add_but.connect("clicked", self.on_add)
        self.main_box.pack_start(self.add_but, True, False, 0)
        self.add_but.show()
        
        self.cancel_but = Gtk.Button("_Cancel", use_underline=True)
        self.cancel_but.connect("clicked", self.on_cancel)
        self.main_box.pack_start(self.cancel_but, True, False, 0)
        self.cancel_but.show()
        
        self.main_box.show()
        
    def on_add(self, widget):
        
        store = self.parent.get_list_store()
        buff = self.task_desc.get_buffer()
        store.append((buff.get_text(buff.get_start_iter(), buff.get_end_iter(), False), False))
        buff.set_text("")
        self.hide()
    
    def on_cancel(self, widget):
        self.hide()
        
        