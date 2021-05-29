#!/usr/bin/python3
import dbus
import dbus.mainloop.glib
# from gi.repository import GLib
from avrcp_manager import AvrcpManager
import pdb


if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    bus = dbus.SystemBus()
    manager = AvrcpManager(bus)

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
        elif cmd == 'exit':
            break

    # mainloop = GLib.MainLoop()
    # mainloop.run()
