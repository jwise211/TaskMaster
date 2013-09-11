from gi.repository import Gtk

class MainWin(Gtk.Window):
    
    def __init__(self):
        #The main window frame
        Gtk.Window.__init__(self, title="Task Master")
        self.connect("delete-event", Gtk.main_quit)
        
        self.main_box = Gtk.Box()
        self.main_box.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(self.main_box)
        
        #The cell renderer
        self.list_store = Gtk.ListStore(str, bool)
        self.list_store.append(["Finish the Dishes", False])
        
        self.tree_view = Gtk.TreeView(self.list_store)
        
        self.text_render = Gtk.CellRendererText()
        self.text_col = Gtk.TreeViewColumn("Task", self.text_render, text=0)
        self.tree_view.append_column(self.text_col)
        
        self.toggle_render = Gtk.CellRendererToggle()
        self.toggle_col = Gtk.TreeViewColumn("Finished", self.toggle_render, active=1)
        self.toggle_render.connect("toggled", self.on_toggle)
        self.tree_view.append_column(self.toggle_col)
        
        self.main_box.add(self.tree_view)
        #The Buttons
        self.add_but = Gtk.Button("Add")
        self.add_but.connect("clicked", self.on_add)
        self.main_box.add(self.add_but)
        
        self.rm_but = Gtk.Button("Remove")
        self.rm_but.connect("clicked", self.on_rm)
        self.main_box.add(self.rm_but)
        
    def on_toggle(self, widget, path):
        self.list_store[path][1] = not self.list_store[path][1]
        
    def on_add(self, widget):
        pass
    
    def on_rm(self, widget):
        pass

win = MainWin()
win.show_all()
Gtk.main()