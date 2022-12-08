#!/bin/bash

export PATH="/home/dani/.local/bin:$PATH"

udiskie -a &
picom --experimental-backend &
eww daemon &
volctl &
nm-applet &
xfce4-power-manager &
mkfifo /tmp/vol-icon && ~/.config/qtile/scripts/vol_icon.sh &
dbus-update-activation-environment DISPLAY XAUTHORITY WAYLAND_DISPLAY
dbus-update-activation-environment --all

# setxkbmap -layout us,us -variant ,intl -option grp:ctrl_shift_toggle &
