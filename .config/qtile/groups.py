from libqtile.config import Group, Key
from pc_type import laptop


def init_groups() -> list[Group]:
    groups = [Group(i) for i in "asd"]
    groups.extend([Group("f",spawn=["signal-desktop","whatsdesk","discord --use-gl=desktop"],layout="verticaltile" if not laptop else None),
    Group("g",spawn="thunderbird"),
    Group("key",spawn=["keepassxc"],label="🔑"),
    ])
    groups.extend([Group(i) for i in"1234"])
    if not laptop:
        groups.extend([Group("5",spawn=["youtube-music" if not laptop else ""])])
    
    return groups



    
