#!/bin/sh

# Volume icone
volumeicon &

# Bluetooth applet
blueman-applet &

# Automount external drives and show a tray (only when there's an action available)
udiskie -s &