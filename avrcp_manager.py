import dbus
import time

# MediaPlayer API: https://github.com/pauloborges/bluez/blob/master/doc/media-api.txt


class AvrcpManager:
    def __init__(self, bus):
        self.bus = bus
        self.player = self.list_devices()

        bus.add_signal_receiver(self.interfaces_added,
                                dbus_interface="org.freedesktop.DBus.ObjectManager",
                                signal_name="InterfacesAdded")

        bus.add_signal_receiver(self.properties_changed,
                                dbus_interface="org.freedesktop.DBus.Properties",
                                signal_name="PropertiesChanged",
                                arg0="org.bluez.Device1",
                                path_keyword="path")

    def list_devices(self):
        proxy = self.bus.get_object('org.bluez', '/')
        manager = dbus.Interface(proxy, dbus_interface='org.freedesktop.DBus.ObjectManager')
        objects = manager.GetManagedObjects()
        for path, interfaces in objects.items():
            if 'org.bluez.MediaPlayer1' in interfaces.keys():
                print(str(path))
                return path

    def interfaces_added(self, path, interfaces):
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

    def properties_changed(self, interface, changed, invalidated, path):
        if interface != "org.bluez.Device1":
            return

        print("properties_changed")
        print(interface)
        print(changed)
        print(invalidated)
        print(path)

    def send_media_command(self, command):
        proxy = self.bus.get_object('org.bluez', self.player)
        iface = dbus.Interface(proxy, dbus_interface='org.bluez.MediaPlayer1')
        method = getattr(iface, command)
        method()

    def status(self):
        pass

    def pause(self):
        self.send_media_command('Pause')

    def resume(self):
        self.send_media_command('Play')

    def next(self):
        self.send_media_command('Next')

    def prev(self):
        self.send_media_command('Previous')
        time.sleep(0.1)
        self.send_media_command('Previous')
