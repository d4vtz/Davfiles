from os import read
from typing import Optional

from core.bar.decorated import Decorations, Powerline
from extras.groupbox import GroupBox
from extras.volume import Volume
from libqtile.bar import CALCULATED
from libqtile.lazy import lazy
from qtile_extras.widget import modify

color = Optional[str]
from core.settings import Colors, colors
from libqtile.widget import TextBox
from qtile_extras import widget


class Widget:
    def __init__(self) -> None:
        self.decorations = Decorations()
        self.powerline = Powerline("arrow")
        self.colors = Colors

    def sep(self, fg: str, padding: int = 8) -> TextBox:
        return TextBox(
            **self.decorations.base(fg),
            **self.decorations.icon_font(),
            padding=padding,
            text="",
        )

    def logo(self, fg: color, bg: color = None) -> TextBox:
        return TextBox(
            **self.decorations.base(fg, bg),
            **self.decorations.decoration(),
            **self.decorations.icon_font(font="Iosevka Nerd Font", size=16),
            mouse_callbacks={"Button1": lazy.restart()},
            padding=17,
            text="",
        )

    def groups(self) -> GroupBox:
        return GroupBox(
            **self.decorations.icon_font(size=16),
            colors=[
                self.colors.home,
                self.colors.web,
                self.colors.code,
                self.colors.read,
                self.colors.music,
                self.colors.media,
                self.colors.social,
                self.colors.system,
            ],
            highlight_color=colors[0],
            highlight_method="line",
            invert=True,
            rainbow=True,
            this_current_screen_border=self.colors.cyan,
            urgent_border=self.colors.alert,
            inactive=self.colors.inactive,
            borderwidth=3,
            disable_drag=True,
            padding_x=3,
            rounded=True,
        )

    def volume(self, bg: str, fg: str) -> list:
        return [
            modify(
                TextBox,
                **self.decorations.base(fg, bg),
                **self.decorations.decoration("left"),
                **self.decorations.icon_font(),
                text="",
                x=4,
            ),
            modify(
                Volume,
                **self.decorations.base(fg, bg),
                **self.decorations.powerline(self.powerline.right),
                commands={
                    "decrease": "pamixer --decrease 5",
                    "increase": "pamixer --increase 5",
                    "get": "pamixer --get-volume-human",
                    "mute": "pamixer --toggle-mute",
                },
                update_interval=0.1,
            ),
        ]

    def updates(self, bg: str, fg: str) -> list:
        return [
            TextBox(
                **self.decorations.base(fg, bg),
                **self.decorations.icon_font(),
                offset=-1,
                text="",
                x=-5,
            ),
            widget.CheckUpdates(
                **self.decorations.base(fg, bg),
                **self.decorations.decoration("right"),
                colour_have_updates=fg,
                colour_no_updates=fg,
                display_format="{updates} updates  ",
                distro="Arch_checkupdates",
                initial_text="No updates  ",
                no_update_string="No updates  ",
                padding=0,
                update_interval=3600,
            ),
        ]

    def window_name(self, bg: str, fg: str) -> object:
        return widget.WindowName(
            **self.decorations.base(fg, bg),
            **self.decorations.decoration("all"),
            format="{name}",
            max_chars=60,
            width=CALCULATED,
            empty_group_string="Desktop",
        )
