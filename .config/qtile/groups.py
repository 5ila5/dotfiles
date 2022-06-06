from libqtile.config import Group, Key


def init_groups() -> list[Group]:
    groups = [Group(i) for i in "asd"]
    groups.extend([Group("f",spawn=["signal-desktop","whatsapp-for-linux","discord --use-gl=desktop"]),
    Group("g",spawn="thunderbird"),
    Group("key",spawn=["keepassxc"],label="🔑"),
    ])
    groups.extend([Group(i) for i in"1234"])
    groups.extend([Group("5",spawn=["spotify"])])

    return groups



    
