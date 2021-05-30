#!/usr/bin/python3
import dbus
import dbus.mainloop.glib
from gi.repository import GLib
from avrcp_manager_lib import AvrcpManager
import pdb
import threading


def handle_input():
    while True:
        cmd = str(input('AVRCP# '))

        if cmd == 'pause':
            manager.pause()
        elif cmd == 'resume' or cmd == 'play':
            manager.resume()
        elif cmd == 'next':
            manager.next()
        elif cmd == 'prev':
            manager.prev()
        elif cmd == 'status':
            manager.status()
        elif cmd == 'exit':
            break


if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    bus = dbus.SystemBus()
    manager = AvrcpManager(bus)
    threading.Thread(target=handle_input).start()

    mainloop = GLib.MainLoop()
    mainloop.run()
