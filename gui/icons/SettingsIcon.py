from gui.icons.ButtonIcon import ButtonIcon


class SettingsIcon(ButtonIcon):

    def callback(self, instance):
        self.parent.state = "Settings"

    def __init__(self, **kwargs):
        super(SettingsIcon, self).__init__("settings", **kwargs)
        self.bind(on_press=self.callback)
