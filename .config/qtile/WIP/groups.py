from libqtile.config import Group, Key


def init_groups() -> list[Group]:
    groups = [Group(i) for i in "asd"]
    groups.extend([Group("f",spawn=["signal-desktop","whatsapp-for-linux","discord --use-gl=desktop"]),
    Group("g",spawn="thunderbird")])
    groups.extend([Group(i) for i in"12345"])
    return groups



    
