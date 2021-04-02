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
bluetoothclt
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

When you need to pair another device, just follow the steps above, starting from the `start on` command.

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
