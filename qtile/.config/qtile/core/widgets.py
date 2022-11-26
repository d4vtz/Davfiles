from libqtile import bar, qtile, lazy

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

from .settings import colors

import os

home = os.path.expanduser("~")

group_box_settings = dict()

# functions for callbacks
def open_launcher():
    qtile.cmd_spawn("rofi -show drun -theme ~/.config/rofi/launcher.rasi")


def open_powermenu():
    qtile.cmd_spawn("" + home + "/.local/bin/power")


def open_calendar():
    qtile.cmd_spawn("" + home + "/home/dani/.local/bin/toggle_cal")


# TODO fix
def toggle_maximize():
    lazy.window.toggle_maximize()


def parse_window_name(text):
    """Simplifies the names of a few windows, to be displayed in the bar"""
    target_names = [
        "Mozilla Firefox",
        "Visual Studio Code",
        "Discord",
    ]
    return next(filter(lambda name: name in text, target_names), text)


class Widgets:
    # widget decorations
    base_decor = {
        "colour": colors[7],
        "filled": True,
        "padding_y": 4,
        "line_width": 0,
    }

    # separator
    def separator(self):
        return widget.Sep(
            # foreground=colors[18],
            foreground=colors[0],
            padding=4,
            linewidth=3,
        )

    def separator_sm(self):
        return widget.Sep(
            # foreground=colors[18],
            foreground=colors[0],
            padding=1,
            linewidth=1,
            size_percent=55,
        )

    def _full_decor(color):
        return [
            RectDecoration(
                colour=color,
                radius=4,
                filled=True,
                padding_y=4,
            )
        ]

    def _left_decor(self, color, padding_x=None, padding_y=4, radius=4):
        return [
            RectDecoration(
                colour=color,
                radius=radius,
                filled=True,
                padding_x=padding_x,
                padding_y=padding_y,
            )
        ]

    # left icon
    def launcher(self):
        return widget.TextBox(
            text="",
            font="Font Awesome 6 Free Solid",
            fontsize=16,
            foreground=colors[4],
            background=colors[0],
            padding=8,
            mouse_callbacks={"Button1": open_launcher},
        )

    def gen_groupbox(self):
        return widget.GroupBox(  # WEB
            font="Font Awesome 6 Free",
            active=colors[7],
            block_highlight_text_color=colors[5],
            this_current_screen_border=colors[7],
            urgent_border=colors[11],
            background=colors[0],
            highlight_color=colors[3],
            inactive=colors[3],
            borderwidth=3,
            disable_drag=True,
            fontsize=16,
            highlight_method="line",
            padding_x=10,
            padding_y=16,
            rounded=True,
        )

    # spacers
    def gen_spacer(self):
        return widget.Spacer()

    # window name
    def w_window_name(self):
        return widget.WindowName(
            foreground="#ffffff",
            width=bar.CALCULATED,
            empty_group_string="Desktop",
            max_chars=40,
            parse_text=parse_window_name,
            mouse_callbacks={"Button1": toggle_maximize},
        )

    # systray
    def w_systray(self):
        return widget.Systray(
            padding=5,
        )

    # current layout
    def gen_current_layout(self):
        color = colors[7]
        return (
            widget.CurrentLayoutIcon(
                custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                padding=3,
                scale=0.65,
                use_mask=True,
                foreground=colors[0],
                decorations=self._left_decor(color, padding_x=2, padding_y=5, radius=0),
            ),
            self.separator(),
        )

    # battery
    def w_battery(self):
        return (
            widget.Battery(
                font="Iosevka Nerd Font",
                format="{char}",
                charge_char="",
                discharge_char="",
                full_char="",
                unknown_char="",
                empty_char="",
                show_short_text=False,
                foreground=colors[4],
                fontsize=19,
                battery_name="BAT0",
                update_interval=1,
            ),
            widget.Battery(
                # font="Iosevka",
                format="{percent:2.0%}",
                show_short_text=False,
                foreground=colors[4],
            ),
        )

    # volume
    def w_volume_icon(self):
        return (
            widget.TextBox(
                text="",
                foreground=colors[4],
                font="Iosevka Nerd Font",
                fontsize=20,
            ),
            widget.PulseVolume(
                foreground=colors[6],
                limit_max_volume="True",
                # font="Iosevka Nerd Font",
                # fontsize=12,
                # mouse_callbacks={"Button3": open_pavu},
            ),
        )

    # internet
    def w_wlan(self):
        return widget.WiFiIcon(
            interface="wlp2s0",
        )

    # time, calendar
    def gen_clock(self):
        color = colors[6]
        return (
            widget.TextBox(
                text="",
                font="Isevka Nerd Font",
                fontsize=20,
                foreground=colors[5],  # blue
                mouse_callbacks={"Button1": open_calendar},
            ),
            self.separator_sm(),
            widget.Clock(
                format="%a %e de %B, %H:%M %p",
                foreground=color,
                mouse_callbacks={"Button1": open_calendar},
            ),
        )

    # power menu
    def w_power(self):
        return widget.TextBox(
            text="⏻",
            background=colors[0],
            foreground=colors[11],
            font="Font Awesome 6 Free Solid",
            fontsize=18,
            mouse_callbacks={"Button1": open_powermenu},
        )
