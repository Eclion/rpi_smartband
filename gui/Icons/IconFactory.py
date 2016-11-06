from gui.Icons.PowerIcon import PowerIcon
from gui.Icons.SettingsIcon import SettingsIcon


def from_name(icon_name):
    if icon_name == "power":
        return PowerIcon()
    if icon_name == "settings":
        return SettingsIcon()
