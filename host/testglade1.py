#!/usr/bin/python3

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def change_label(button):
    button.set_label('d')


if __name__ == '__main__':

    builder = Gtk.Builder()

    gladefile = ('/home/yoel/Documents/Proyecto-Python/widgets/try.glade')

    builder.add_from_file(gladefile)

    win = builder.get_object('main_window')


    button11 = builder.get_object('11')
    button12 = builder.get_object('12')
    button13 = builder.get_object('13')

    button21 = builder.get_object('21')
    button22 = builder.get_object('22')
    button23 = builder.get_object('23')

    button31 = builder.get_object('31')
    button32 = builder.get_object('32')
    button33 = builder.get_object('33')

   


    button11.connect('clicked', change_label)
    button12.connect('clicked', change_label)
    button13.connect('clicked', change_label)

    button21.connect('clicked', change_label)
    button22.connect('clicked', change_label)
    button23.connect('clicked', change_label)

    button31.connect('clicked', change_label)
    button32.connect('clicked', change_label)
    button33.connect('clicked', change_label)



    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

