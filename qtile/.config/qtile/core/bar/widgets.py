import os
from typing import Optional

from core.bar.decorated import Decorations, Powerline
from extras.clock import Clock
from extras.groupbox import GroupBox
from extras.volume import Volume
from libqtile.bar import CALCULATED
from libqtile.lazy import lazy
from qtile_extras.widget import modify

color = Optional[str]
from core.settings import Colors
# from libqtile import widget
from libqtile.widget import CurrentLayoutIcon, TextBox
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
            **self.decorations.decoration("all"),
            **self.decorations.icon_font(font="Iosevka Nerd Font", size=16),
            mouse_callbacks={"Button1": lazy.restart()},
            padding=12,
            text="    ",
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
            highlight_color=self.colors.background,
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
        base = self.decorations.base(fg, bg)
        return [
            widget.TextBox(
                **base,
                **self.decorations.decoration("left"),
                **self.decorations.icon_font(),
                text="",
            ),
            modify(
                Volume,
                **base,
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
                text="",
                x=-5,
            ),
            widget.CheckUpdates(
                **self.decorations.base(fg, bg),
                **self.decorations.powerline(self.powerline.right),
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

    def window_name(self) -> widget.WindowName:
        return widget.WindowName(
            format="{name}",
            max_chars=60,
            width=CALCULATED,
            empty_group_string="Desktop",
        )

    def clock(self, bg: str, fg: str) -> list:
        return [
            modify(
                TextBox,
                **self.decorations.base(fg, bg),
                **self.decorations.icon_font(),
                text="",
            ),
            modify(
                Clock,
                **self.decorations.base(fg, bg),
                **self.decorations.decoration("right"),
                format="%A  %-I:%M %p ",
                long_format="%-d de %B del %Y ",
                padding_x=-15,
            ),
        ]

    def gen_current_layout(self):
        return widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            padding=3,
            scale=0.65,
            use_mask=True,
            foreground=self.colors.white,
        )

    @property
    def widgets(self):
        return [
            self.logo(fg=self.colors.cyan, bg=self.colors.gray),
            self.sep(fg=self.colors.gray),
            self.gen_current_layout(),
            self.sep(fg=self.colors.gray),
            self.groups(),
            widget.Spacer(),
            self.window_name(),
            widget.Spacer(),
            *self.volume(bg=self.colors.cyan, fg=self.colors.gray),
            *self.updates(bg="#f2d2aa", fg="#11111B"),
            *self.clock(bg=self.colors.white, fg=self.colors.black),
        ]
