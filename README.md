## Customization

To have a graphical interface to manage all the themes/icons, install [lxappearance](https://archlinux.org/packages/community/x86_64/lxappearance/).

### Themes

Download the theme and copy the folder in `/usr/share/themes`. Edit [`~/.gtkrc-2.0`](./.gtkrc-2.0) and [`~/.config/gtk-3.0/settings.ini`](./.config/gtk-3.0/settings.ini) and change gtk-theme-name. Close session to apply the changes.

### Icons and cursors

Download the icon/cursor theme and copy the folder in `/usr/share/icons`. Edit [`~/.gtkrc-2.0`](./.gtkrc-2.0) and [`~/.config/gtk-3.0/settings.ini`](./.config/gtk-3.0/settings.ini) and change gtk-icon-theme-name (for icons) and gtk-cursor-theme-name (for cursors). Close session to apply the changes.

If you want to change the cursor theme, you will also need to edit `/usr/share/themes/default/index.theme`:

<pre>
[Icon Theme]
Inherits=<i>your_theme</i>
</pre>

Besides, if you are using qtile you have to install [xcb-util-cursor](https://archlinux.org/packages/extra/x86_64/xcb-util-cursor/) to apply the changes.

In my case, I installed [Material-black COLORS](https://www.gnome-look.org/p/1316887/) theme, [Material-black COLORS](https://www.pling.com/p/1333360/) icons and [Breeze](https://www.gnome-look.org/p/999927/) cursors.

## Bluetooth

The following instructions can be used to connect to any bluetooth device, including bluetooth headsets.

Install the following packages: [bluez](https://archlinux.org/packages/extra/x86_64/bluez/), [bluez-utils](https://archlinux.org/packages/extra/x86_64/bluez-utils/), [pulseaudio-alsa](https://archlinux.org/packages/extra/x86_64/pulseaudio-alsa/), [pulseaudio-bluetooth](https://archlinux.org/packages/extra/x86_64/pulseaudio-bluetooth/).

If you also want a graphical interface to manage bluetooth connectivity, install [blueman](https://archlinux.org/packages/community/x86_64/blueman/).

Before using the bluetooth device, make sure that it is not blocked by [rfkill](https://wiki.archlinux.org/index.php/Network_configuration/Wireless#Rfkill_caveat). Run `rfkill list` to check it. If you want to unblock everything, run `rfkill unblock all`, or just unblock the one you need.

First, start the bluetooth.service systemd unit. Run:

```
sudo systemctl start bluetooth.service
sudo systemctl enable bluetooth.service
```

Use the bluetoothctl command line utility to pair and connect

```
bluetoothctl
```

to be greeted by its internal command prompt. Then enter:

```
[bluetooth]# power on
[bluetooth]# agent on
[bluetooth]# default-agent
[bluetooth]# scan on
```

Now make sure that the bluetooth device you want to connect is in pairing mode. It should be discovered shortly. Copy its MAC address and enter the following commands (or start typing the MAC address and press tab to autocomplete it):

<pre>
[bluetooth]# pair <i>MAC_address</i>
[bluetooth]# connect <i>MAC_address</i>
[bluetooth]# trust <i>MAC_address</i>
</pre>

Finally, you can switch off the scanning.

```
scan off
```

When you need to pair another device, just follow the steps above, starting from the `scan on` command. To exit, type `exit`.

By default, the Bluetooth adapter does not power on after a reboot, you need to add the line `AutoEnable=true` in the configuration file `/etc/bluetooth/main.conf` at the bottom in the `[Policy]` section:

```
[Policy]
AutoEnable=true
```

To make your headset auto connect you need to enable PulseAudio's switch-on-connect module. Do this by adding the following lines to `/etc/pulse/default.pa`:

```
### Automatically switch to newly-connected devices
load-module module-switch-on-connect
```

For further info and troubleshooting, check the ArchWiki [here](https://wiki.archlinux.org/index.php/Bluetooth) and [here](https://wiki.archlinux.org/index.php/Bluetooth_headset).

## Video drivers

Although Xorg already comes with a generic video driver, it's important to install the correct one for your GPU to get the best performance. Check [here](https://wiki.archlinux.org/index.php/xorg#Driver_installation) which is the one you need.

## Notifications

Install [libnotify](https://archlinux.org/packages/extra/x86_64/libnotify/) and [notification-daemon](https://archlinux.org/packages/community/x86_64/notification-daemon/). Then, in `/usr/share/dbus-1/services` create the file `org.freedesktop.Notifications.service`if it doesn't already exist, and add the following lines to it:

```
[D-BUS Service]
Name=org.freedesktop.Notifications
Exec=/usr/lib/notification-daemon-1.0/notification-daemon
```

Close session and after login notifications should be working. More [info](https://wiki.archlinux.org/index.php/Desktop_notifications).

## System tray icons

- Bluetooth: comes preinstalled with [blueman](https://archlinux.org/packages/community/x86_64/blueman/).
- Volume: [volumeicon](https://archlinux.org/packages/community/x86_64/volumeicon/).
- Network: [network-manager-applet](https://archlinux.org/packages/extra/x86_64/network-manager-applet/). Requires [networkmanager](https://archlinux.org/packages/extra/x86_64/networkmanager/).
- Battery: [cbatticon](https://archlinux.org/packages/community/x86_64/cbatticon/)
- Notifications: check the notifications section. The icon will appear automatically.

Then, add [these](./.config/qtile/autostart.sh) lines to `~/.config/qtile/autostart.sh` so that the icons are initialized when you login.
