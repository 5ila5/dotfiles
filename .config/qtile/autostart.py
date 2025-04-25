from libqtile import qtile
import os
from libqtile import hook
import subprocess
import get_core
from pc_type import laptop
from wayland_env_vars import WAYLAND_ENV_VARS
from pathlib import Path

desktop_dir = (
    Path(os.path.dirname(os.path.realpath(__file__))) / ".." / "desktop"
).resolve()

print(desktop_dir)


def autostart():

    home = os.path.expanduser(desktop_dir / "autostart.sh")
    subprocess.run([home])

    if get_core.get_core_name() == "wayland":
        home = os.path.expanduser(desktop_dir / "autostart_wayland.sh")
        os.environ.update(WAYLAND_ENV_VARS)
    else:
        home = os.path.expanduser(desktop_dir / "autostart_X11.sh")
    subprocess.run([home])

    subprocess.run(
        [
            "dbus-update-activation-environment",
            "--systemd",
            "WAYLAND_DISPLAY",
            "XDG_CURRENT_DESKTOP",
        ]
    )
