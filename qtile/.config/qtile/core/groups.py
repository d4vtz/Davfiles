from libqtile.config import DropDown, Group, Key, Match, ScratchPad
from libqtile.lazy import lazy

from .keys import keys, mod, shift

workspace_names = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]
groups = [
    Group(
        name="Home",
        label="",
    ),
    Group(
        name="Web",
        label="",
        matches=[Match(wm_class="google-chrome")],
    ),
    Group(
        name="Code",
        label="",
        matches=[Match(wm_class="code")],
    ),  #   
    Group(
        name="Physic",
        label="",
        matches=[Match(wm_class="Zathura")],
        layout="looking good",
    ),
    Group(
        name="Music",
        label="",
    ),
    Group(
        name="Media",
        label=" ",
    ),
    Group(
        name="Social",
        label="",
    ),
    Group(
        name="System",
        label="",
        matches=[Match(wm_class="pavucontrol")],
    ),
]

for index, group in enumerate(groups, start=1):
    keys.append(
        Key(
            [mod],
            str(index),
            lazy.group[group.name].toscreen(),
            desc="Focus this desktop",
        )
    )
    keys.append(
        Key(
            [mod, shift],
            str(index),
            lazy.window.togroup(group.name),
            lazy.group[group.name].toscreen(),
            desc="Move focused window to another group",
        )
    )

kitty_scratchpad = dict(
    opacity=1,
    x=0.1,
    y=0.15,
    width=0.8,
    height=0.7,
    on_focus_lost_hide=True,
)

groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown("term", "kitty", **kitty_scratchpad),
        ],
    )
)
