from core.bar.widgets import Widget
from libqtile import bar
from libqtile.config import Screen

from .settings import colors, wallpaper_main
from .widgets import Widgets

widgets = Widget()
widget_defaults = dict(
    font="Roboto Condense",
    fontsize=12,
    background=colors[0],
)
extension_defaults = widget_defaults.copy()


def create_bar():
    """Create top bar, defined as function to allow duplication in other monitors"""
    widget = Widgets()
    return bar.Bar(
        [
            # widget.launcher(),
            # widget.gen_groupbox(),
            # widget.gen_spacer(),
            # widget.w_window_name(),
            # widget.gen_spacer(),
            widget.w_systray(),
            # widget.separator(),
            # *widget.gen_current_layout(),
            # *widget.gen_clock(),
            # widget.w_power(),
            # wid.Spacer(length=2),
            widgets.logo(fg="#00ffff"),
            widgets.sep(fg="#ffffff"),
            widgets.groups(bg=colors[0]),
            widget.gen_spacer(),
            widgets.window_name(fg=colors[0], bg="#eee86e"),
            widget.gen_spacer(),
            *widgets.volume(bg="#bb0fff", fg="#000"),
            *widgets.updates(bg="#f2d2aa", fg="#11111B"),
        ],
        26,
        margin=[10, 8, 8, 10],
        background=colors[0],
    )


screens = [
    Screen(
        wallpaper=wallpaper_main,
        wallpaper_mode="fill",
        top=create_bar(),
        bottom=bar.Gap(2),
        left=bar.Gap(2),
        right=bar.Gap(2),
    ),
]
