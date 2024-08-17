import os

from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from utils.functions import (
    backlight,
    resize_down,
    resize_left,
    resize_right,
    resize_up,
    float_to_front,
)

mod = "mod4"
control = "control"
shift = "shift"
alt = "mod1"


class Keymode:
    def __init__(self, mode: str) -> None:

        if mode == "VIM":
            self.RIGHT = "l"
            self.LEFT = "h"
            self.UP = "k"
            self.DOWN = "j"
        else:
            self.RIGHT = "Right"
            self.LEFT = "Left"
            self.UP = "Up"
            self.DOWN = "Down"


mode = Keymode(mode="VIM")

terminal = guess_terminal()
home = os.path.expanduser("~")
keys = [
    # essentials
    # Key([mod], "y", lazy.layout.hide()),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "q", lazy.window.kill(), desc="Kill active window"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle forward layout"),
    Key([mod, shift], "Tab", lazy.prev_layout(), desc="Toggle last layout"),
    # qtile
    Key([mod, shift], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, shift], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # menus
    Key(
        [mod, shift],
        "Return",
        lazy.spawn("rofi -show drun -theme ~/.config/rofi/launcher.rasi"),
        desc="Launch Rofi",
    ),
    Key(
        [mod, shift],
        "e",
        lazy.spawn("" + home + "/.local/bin/power"),
        desc="Power Menu",
    ),
    Key(
        [mod, shift],
        "n",
        lazy.spawn("" + home + "/.local/bin/nmgui"),
        desc="Network Menu",
    ),
    # focus, move windows and screens
    Key(
        [mod],
        mode.DOWN,
        lazy.layout.down(),
        desc="Move focus down in current stack pane",
    ),
    Key([mod], mode.UP, lazy.layout.up(), desc="Move focus up in current stack pane"),
    Key(
        [mod],
        mode.LEFT,
        lazy.layout.left(),
        desc="Move focus left in current stack pane",
    ),
    Key(
        [mod],
        mode.RIGHT,
        lazy.layout.right(),
        desc="Move focus right in current stack pane",
    ),
    Key(
        [mod, shift],
        mode.DOWN,
        lazy.layout.shuffle_down(),
        lazy.layout.move_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [mod, shift],
        mode.UP,
        lazy.layout.shuffle_up(),
        lazy.layout.move_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [mod, shift],
        mode.LEFT,
        lazy.layout.shuffle_left(),
        lazy.layout.move_left(),
        desc="Move windows left in current stack",
    ),
    Key(
        [mod, shift],
        mode.RIGHT,
        lazy.layout.shuffle_right(),
        lazy.layout.move_right(),
        desc="Move windows right in the current stack",
    ),
    Key(
        [mod],
        "x",
        lazy.next_screen(),
        desc="Move focus to next monitor",
    ),  # TODO find a better hotkey
    Key([mod, control], mode.DOWN, lazy.layout.flip_down(), desc="Flip layout down"),
    Key([mod, control], mode.UP, lazy.layout.flip_up(), desc="Flip layout up"),
    Key(
        [mod, control],
        mode.LEFT,
        lazy.layout.flip_left(),
        lazy.layout.swap_column_left(),
        desc="Flip layout left",
    ),
    Key(
        [mod, control],
        mode.RIGHT,
        lazy.layout.flip_right(),
        lazy.layout.swap_column_left(),
        desc="Flip layout right",
    ),
    # window resizing
    Key([mod, alt], mode.LEFT, resize_left, desc="Resize window left"),
    Key([mod, alt], mode.RIGHT, resize_right, desc="Resize window Right"),
    Key([mod, alt], mode.UP, resize_up, desc="Resize windows upward"),
    Key([mod, alt], mode.DOWN, resize_down, desc="Resize windows downward"),
    Key([mod, alt], "n", lazy.layout.normalize(), desc="Normalize window size ratios"),
    # window states
    Key(
        [mod],
        "m",
        lazy.window.toggle_maximize(),
        desc="Toggle window between minimum and maximum sizes",
    ),
    Key([mod, shift], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key(
        [mod],
        "i",
        lazy.window.toggle_floating(),
        desc="Toggle floating mode for a window",
    ),
    Key([], "F11", lazy.window.toggle_fullscreen()),
    # Floating window management
    Key([mod], "space", lazy.window.toggle_floating()),
    Key([mod], "c", lazy.window.center()),
    Key([mod], "f", lazy.function(float_to_front)),
    # program launches
    Key([mod], "w", lazy.spawn("google-chrome-stable"), desc="Launch Google Chrome"),
    Key([mod], "e", lazy.spawn("thunar"), desc="Launch Thunar"),
    Key([mod], "s", lazy.spawn("spotify"), desc="Launch Spotify"),
    Key([mod], "t", lazy.group["scratchpad"].dropdown_toggle("term")),
    # screenshots
    Key(
        [],
        "Print",
        lazy.spawn("" + home + "/.local/bin/prtscreen"),
        desc="Print Screen",
    ),
    Key(
        [mod],
        "Print",
        lazy.spawn("" + home + "/.local/bin/prtscreenregion"),
        desc="Print region of screen",
    ),
    Key(
        [mod, shift],
        "s",
        lazy.spawn("" + home + "/.local/bin/prtscreenregion"),
        desc="Print region of screen",
    ),
    # audio stuff
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("./.config/qtile/scripts/temp_vol.sh up"),
        desc="Increase volume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("./.config/qtile/scripts/temp_vol.sh down"),
        desc="Decrease volume",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("./.config/qtile/scripts/temp_vol.sh mute"),
        desc="Toggle volume mute",
    ),
    Key(
        [],
        "XF86AudioPrev",
        lazy.spawn("playerctl previous"),
        desc="Play last audio",
    ),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Play next audio"),
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc="Toggle play/pause audio",
    ),
    # Key([mod], "F8", lazy.spawn("playerctl stop"), desc="Stop audio"),
    # eww
    Key(
        [mod],
        "d",
        lazy.spawn("" + home + "/.local/bin/toggle_eww"),
        desc="Toggle eww dashboard",
    ),
    # brightness
    Key([mod], "Prior", lazy.function(backlight("inc")), desc="Increase brightness"),
    Key([mod], "Next", lazy.function(backlight("dec")), desc="Decrease brightness"),
    # LayoutKey
    Key(
        [mod, shift],
        "k",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Swich layout key",
    ),
]


def show_keys():
    key_help = ""
    for k in keys:
        mods = ""

        for m in k.modifiers:
            if m == "mod4":
                mods += "Super + "
            else:
                mods += m.capitalize() + " + "

        if len(k.key) > 1:
            mods += k.key.capitalize()
        else:
            mods += k.key

        key_help += "{:<25} {}".format(mods, k.desc + "\n")

    return key_help


keys.extend(
    [
        Key(
            [mod],
            "a",
            lazy.spawn(
                "sh -c 'echo \""
                + show_keys()
                + '" | rofi -dmenu -theme ~/.config/rofi/configTall.rasi -i -p ""\''
            ),
            desc="Print keyboard bindings",
        ),
    ]
)
