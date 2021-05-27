#!/usr/bin/python3
import dbus
import dbus.mainloop.glib
from gi.repository import GLib
import pdb

def interfaces_added(path, interfaces):
    print(interfaces.keys())
    if "org.bluez.MediaPlayer1" not in interfaces:
        return

    media_player = interfaces["org.bluez.MediaPlayer1"]

    if "Device" not in media_player:
        return

    device = media_player["Device"]

    print("interfaces_added")
    print(path)
    print(str(device))

def properties_changed(interface, changed, invalidated, path):
    if interface != "org.bluez.Device1":
        return

    print("properties_changed")
    print(interface)
    print(changed)
    print(invalidated)
    print(path)

def pause(bus):
    proxy = bus.get_object('org.bluez', '/org/bluez/hci0/dev_F8_2D_7C_A1_EF_2F')
    iface = dbus.Interface(proxy, dbus_interface='org.bluez.MediaControl1')
    props = iface.Pause()

def play(bus):
    proxy = bus.get_object('org.bluez', '/org/bluez/hci0/dev_F8_2D_7C_A1_EF_2F')
    iface = dbus.Interface(proxy, dbus_interface='org.bluez.MediaControl1')
    props = iface.Play()

if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    bus = dbus.SystemBus()
    bus.add_signal_receiver(interfaces_added,
            dbus_interface = "org.freedesktop.DBus.ObjectManager",
            signal_name = "InterfacesAdded")

    bus.add_signal_receiver(properties_changed,
            dbus_interface = "org.freedesktop.DBus.Properties",
            signal_name = "PropertiesChanged",
            arg0 = "org.bluez.Device1",
            path_keyword = "path")

    play(bus)

    mainloop = GLib.MainLoop()
    mainloop.run()
