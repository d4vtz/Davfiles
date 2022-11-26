from libqtile import bar
from libqtile.config import Screen


from .widgets import Widgets
from .settings import colors, wallpaper_main


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
            widget.launcher(),
            widget.gen_groupbox(),
            widget.gen_spacer(),
            widget.w_window_name(),
            widget.gen_spacer(),
            widget.w_systray(),
            widget.separator(),
            *widget.gen_current_layout(),
            *widget.gen_clock(),
            widget.w_power(),
        ],
        26,
        margin=[10, 6, 6, 10],
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
