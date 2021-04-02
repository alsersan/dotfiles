#!/bin/sh

# Network Manager applet
nm-applet &

# Volume icon
volumeicon &

# Bluetooth applet
blueman-applet &

# Automount external drives and show a tray (only when there's an action available)
udiskie -s &