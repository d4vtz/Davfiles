import os
import subprocess

from libqtile import hook

from core.groups import groups
from core.keys import keys, mod, shift
from core.layouts import floating_layout, layouts
from core.screens import screens, widget_defaults

# REVIEW options
auto_fullscreen = True
auto_minimize = False
bring_front_click = False
cursor_warp = False
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
focus_on_window_activation = "smart"
reconfigure_screens = True
wl_input_rules = None
wmname = "qtile"


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])
