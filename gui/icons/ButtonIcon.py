from os.path import dirname
from os.path import join

from kivy.uix.button import Button
from kivy.uix.image import Image


class ButtonIcon(Button):
    # def __init__(self, icon_name, **kwargs):
    #    super(ButtonIcon, self).__init__(**kwargs)
    #    icon_path = glob(join(dirname(__file__), "resources", icon_name+".svg"))
    #    with self.canvas:
    #        svg = Svg(icon_path)
    #    self.size = 20, 20
    icon = None

    def on_pos(self, instance, value):
        self.icon.pos = value

    def on_size(self, instance, value):
        self.icon.size = value

    def __init__(self, icon_name, **kwargs):
        super(ButtonIcon, self).__init__(**kwargs)
        icon_path = join(dirname(__file__), "resources", icon_name + ".png")
        self.icon = Image(source=str(icon_path))
        self.add_widget(self.icon)
        self.background_color = (0, 0, 0, 0)
