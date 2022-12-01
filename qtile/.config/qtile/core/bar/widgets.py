from typing import Optional

from core.bar.decorated import BarTheme
from extras.groupbox import GroupBox
from extras.volume import Volume
from libqtile.bar import CALCULATED
from libqtile.lazy import lazy
from qtile_extras.widget import modify

color = Optional[str]
from core.settings import colors
from libqtile.widget import TextBox
from qtile_extras import widget

# from extras.textbox import TextBox


class Widget:
    def __init__(self) -> None:
        self.theme = BarTheme()

    def sep(self, fg: str, offset=0, padding=8) -> TextBox:
        return TextBox(
            **self.theme.base(fg),
            **self.theme.icon_font(),
            offset=offset,
            padding=padding,
            text="",
        )

    def logo(self, fg: color, bg: color = None) -> TextBox:
        return modify(
            TextBox,
            **self.theme.base(fg, bg),
            **self.theme.decoration(),
            **self.theme.icon_font(),
            mouse_callbacks={"Button1": lazy.restart()},
            offset=4,
            padding=17,
            text="",
        )

    def groups(self, bg: str) -> GroupBox:
        return GroupBox(
            **self.theme.icon_font(15),
            background=bg,
            colors=[
                colors[8],
                colors[13],
                colors[4],
                colors[15],
                colors[14],
                colors[10],
                colors[3],
            ],
            highlight_color=colors[0],
            highlight_method="line",
            invert=True,
            rainbow=True,
            this_current_screen_border=colors[7],
            urgent_border=colors[11],
            inactive=colors[3],
            borderwidth=3,
            disable_drag=True,
            padding_x=10,
            rounded=True,
        )

    def volume(self, bg: str, fg: str) -> list:
        return [
            modify(
                TextBox,
                **self.theme.base(fg, bg),
                **self.theme.decoration("left"),
                **self.theme.icon_font(),
                text="",
                x=4,
            ),
            modify(
                Volume,
                **self.theme.base(fg, bg),
                **self.theme.powerline("arrow_right"),
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
                **self.theme.base(fg, bg),
                **self.theme.icon_font(),
                offset=-1,
                text="",
                x=-5,
            ),
            widget.CheckUpdates(
                **self.theme.base(fg, bg),
                **self.theme.decoration("right"),
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
            **self.theme.base(fg, bg),
            **self.theme.decoration("all"),
            format="{name}",
            max_chars=60,
            width=CALCULATED,
            empty_group_string="Desktop",
        )
