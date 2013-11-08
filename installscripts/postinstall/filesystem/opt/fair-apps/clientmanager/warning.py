import gtk

class WarningWindow(gtk.Window):
    
    def __init__(self):
        super(WarningWindow, self).__init__()
        self.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        self.set_decorated(False)
        self.set_modal(True)
        hpanel = gtk.HBox(1)
        vpanel = gtk.VBox(2)
        vpanel.pack_start(
            gtk.Label("Your session is 5 minutes from running out. \nSave your documents on a portable media or you will lose them."),
            padding=20
        )
        close = gtk.Button("Close", stock=gtk.STOCK_CLOSE)
        close.connect("clicked", self.on_delete_event)
        vpanel.pack_start(
            close,
            padding=20
        )
        hpanel.pack_start(vpanel, padding=20)
        self.connect("delete-event", self.on_delete_event)
        self.connect('destroy', self.on_delete_event)
        self.add(hpanel)
        self.show_all()

    def on_delete_event(self, *args):
        """
        Display manager closed window.
        """
        self.destroy()
        gtk.main_quit()


if __name__ == '__main__':
    
    mainwindow = WarningWindow()
    gtk.main()
