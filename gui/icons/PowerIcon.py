from gui.icons.ButtonIcon import ButtonIcon


class PowerIcon(ButtonIcon):

    def callback(self, instance):
        print('powaaa')
        exit()

    def __init__(self, **kwargs):
        super(PowerIcon, self).__init__("power", **kwargs)
        self.bind(on_press=self.callback)
