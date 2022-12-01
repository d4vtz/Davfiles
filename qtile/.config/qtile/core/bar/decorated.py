from typing import Optional

from core.settings import colors
from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration

color = Optional[str]


class BarTheme:
    def __init__(self) -> None:
        pass

    def base(self, fg: color, bg: color = None) -> dict:
        if bg is None:
            bg = colors[0]
        return {
            "background": bg,
            "foreground": fg,
        }

    def decoration(self, side: str = "", width: int = 10) -> dict:
        return {
            "decorations": [
                RectDecoration(
                    filled=True,
                    radius={
                        "left": [width, 0, 0, width],
                        "right": [0, width, width, 0],
                        "all": [width for _ in range(4)],
                    }.get(side, width),
                    use_widget_background=True,
                )
            ]
        }

    @staticmethod
    def icon_font(size: int = 14) -> dict:
        return {"font": "Font Awesome 6 Free Solid", "fontsize": size}

    @staticmethod
    def powerline(path: str | list, size=9) -> dict:
        return {
            "decorations": [
                PowerLineDecoration(
                    path=path,
                    size=size,
                )
            ]
        }
