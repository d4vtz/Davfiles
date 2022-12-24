from typing import Dict, Optional

color = Optional[str]


class ThemeSettings:
    @staticmethod
    def font(
        size: int = 14, font: str = "Font Awesome 6 Free Solid"
    ) -> dict[str, str | int]:
        return {"font": font, "fontsize": size}

    @staticmethod
    def ground_colors(fg: color, bg: color = None) -> Dict[str, color]:
        if bg is None:
            return {
                "foreground": fg,
            }
        return {
            "background": bg,
            "foreground": fg,
        }
