from typing import Dict, Optional

from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration

color = Optional[str]


class Powerline:
    def __init__(self, shape: str) -> None:
        if shape in ["arrow", "rounded", "slash"]:
            self.shape = shape
        else:
            self.shape = "arrow"

    @property
    def right(self) -> str:
        if self.shape == "slash":
            return f"{self.shape}_right"
        return f"forward_{self.shape}"

    @property
    def left(self) -> str:
        if self.shape == "slash":
            return f"{self.shape}_left"
        return f"back_{self.shape}"


class Decorations:
    @staticmethod
    def icon_font(
        size: int = 14, font: str = "Font Awesome 6 Free Solid"
    ) -> dict[str, str | int]:
        return {"font": font, "fontsize": size}

    @staticmethod
    def base(fg: color, bg: color = None) -> Dict[str, color]:
        if bg is None:
            return {
                "foreground": fg,
            }
        return {
            "background": bg,
            "foreground": fg,
        }

    @staticmethod
    def decoration(
        side: str = "all", width: int = 10
    ) -> Dict[str, list[RectDecoration]]:
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
                    group=True,
                    clip=True,
                )
            ]
        }

    @staticmethod
    def powerline(
        path: str, size=7, shift: int = -15
    ) -> dict[str, list[PowerLineDecoration]]:
        return {"decorations": [PowerLineDecoration(path=path, size=size, shift=shift)]}
