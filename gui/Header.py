from kivy.properties import StringProperty, DictProperty, ObjectProperty
# from kivy.graphics.svg import Svg
from kivy.uix.widget import Widget

from gui.icons import IconFactory


class Header(Widget):
    state = StringProperty()
    icons = DictProperty()

    def __init__(self, **kwargs):
        super(Header, self).__init__(**kwargs)
        self.enable_icon('power')
        self.enable_icon('settings')

    def on_state(self, instance, value):
        truc = self.ids['state_label']
        pass

    def on_pos(self, instance, value):
        self.refresh()

    def on_size(self, instance, value):
        self.refresh()

    def on_icons(self, instance, value):
        pass

    def enable_icon(self, icon_name):
        if icon_name not in self.icons:
            self.icons[icon_name] = {'enabled': True, 'index': len(self.icons), 'widget': IconFactory.from_name(icon_name)}
        elif self.icons[icon_name]['enabled']:
            pass
        else:
            self.icons[icon_name]['enabled'] = True
            if self.icons[icon_name]['widget'] is None:
                self.icons[icon_name]['widget'] = IconFactory.from_name(icon_name)
        self.add_widget(self.icons[icon_name]['widget'])
        self.refresh()

    def disable_icon(self, icon_name):
        if icon_name not in self.icons or not self.icons[icon_name]['enabled']:
            pass

        self.icons[icon_name]['enabled'] = False
        self.remove_widget(self.icons[icon_name]['widget'])
        self.refresh()

    def refresh(self):
        size = self.height / 2
        for icon in (i for i in self.icons if self.icons[i]['enabled']):
            index = self.icons[icon]['index']
            x = self.width - size * 5 / 4 - index * size * 1 / 2 - index * size
            y = self.y + self.height / 2 - size / 2
            self.icons[icon]['widget'].size = size, size
            self.icons[icon]['widget'].pos = x, y
