import os
from typing import Optional

from core.bar.decorated import ThemeSettings
from extras.clock import Clock
from extras.groupbox import GroupBox
from extras.updates import CheckUpdate
from libqtile.bar import CALCULATED
from libqtile.lazy import lazy
from qtile_extras.widget import modify

color = Optional[str]
from core.settings import Colors
# from libqtile import widget
from libqtile.widget import TextBox
from qtile_extras import widget


class Widget:
    def __init__(self) -> None:
        self.settings = ThemeSettings()
        self.colors = Colors

    def sep(self, fg: str, padding: int = 8) -> TextBox:
        return TextBox(
            **self.settings.ground_colors(fg),
            **self.settings.font(),
            padding=padding,
            text="",
        )

    def logo(self, fg: color) -> TextBox:
        return TextBox(
            **self.settings.ground_colors(fg),
            **self.settings.font(font="Iosevka Nerd Font", size=16),
            mouse_callbacks={"Button1": lazy.restart()},
            padding=12,
            text="    ",
        )

    def groups(self) -> GroupBox:
        return GroupBox(
            **self.settings.font(size=16),
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

    def updates(self, fg: str) -> list:
        return [
            TextBox(
                **self.settings.ground_colors(fg),
                **self.settings.font(),
                text="",
            ),
            modify(
                CheckUpdate,
                **self.settings.ground_colors(fg),
                colour_have_updates=fg,
                colour_no_updates=fg,
                display_format="{updates} updates  ",
                distro={"pacman":"checkupdates", "aur": "paru -Qu"},
                initial_text="No updates  ",
                no_update_string="No updates  ",
                execute=True,
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

    def clock(self, fg: str) -> list:
        return [
            TextBox(
                **self.settings.ground_colors(fg),
                **self.settings.font(),
                text="",
            ),
            Clock(
                **self.settings.ground_colors(fg),
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

    def exit(self, fg: str):
        return widget.TextBox(
            **self.settings.ground_colors(fg),
            **self.settings.font(font="Iosevka Nerd Font", size=16),
            mouse_callbacks={"Button1": lazy.restart()},
            padding=12,
            text="   ",
        )

    def status_notifier(self):
        return widget.StatusNotifier(
            icon_size=24,
            icon_theme="/usr/share/icons/Papirus",
            padding=10,
            hide_after=5,
            menu_width=250,
            show_menu_icons=True,
            background=self.colors.background,
            highlight_colour=self.colors.gray,
            menu_background=self.colors.background,
            menu_foreground=self.colors.white,
            menu_foreground_disabled=self.colors.red,
            menu_icon_size=16,
            menu_fontsize=16,
            menu_foreground_highlighted=self.colors.violet,
            highlight_radius=7.5,
            separator_colour=self.colors.gray,
            menu_border=self.colors.white,
            menu_border_width=1,
            menu_offset_x=2,
            menu_offset_y=6,
        )

    @property
    def widgets(self):
        return [
            self.logo(fg=self.colors.cyan),
            self.sep(fg=self.colors.gray),
            self.gen_current_layout(),
            self.sep(fg=self.colors.gray),
            self.groups(),
            widget.Spacer(),
            self.window_name(),
            widget.Spacer(),
            widget.Systray(padding=8),
            self.status_notifier(),
            self.sep(fg=self.colors.gray),
            widget.KeyboardLayout(configured_keyboards=["us", "us intl"], display_map={"us": "us", "us intl": "US"}),
            *self.updates(fg=self.colors.foreground),
            *self.clock(fg=self.colors.foreground),
            self.sep(fg=self.colors.gray),
            self.exit(fg=self.colors.red),
        ]
