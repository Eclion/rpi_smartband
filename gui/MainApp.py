from kivy.app import App
# from kivy.graphics.svg import Svg
from kivy.properties import NumericProperty, ObjectProperty, StringProperty, ListProperty, DictProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window

from gui.Icons import ButtonIcon
from gui.Icons import IconFactory
from gui.Icons.PowerIcon import PowerIcon


class Header(Widget):
    state = StringProperty("Menu")
    icons = DictProperty()

    def on_pos(self, instance, value):
        self.refresh()

    def on_size(self, instance, value):
        self.refresh()

    def __init__(self, **kwargs):
        super(Header, self).__init__(**kwargs)
        #power_icon = PowerIcon()
        #self.icons['power'] = {'enabled': True, 'widget': power_icon}
        self.enable_icon('power')
        self.enable_icon('settings')

    def on_icons(self, instance, value):
        pass

    def enable_icon(self, icon_name):
        if icon_name not in self.icons:
            self.icons[icon_name] = {'enabled': True, 'widget': IconFactory.from_name(icon_name)}
        elif self.icons[icon_name]['enabled']:
            pass
        else:
            self.icons[icon_name]['enabled'] = True
        self.add_widget(self.icons[icon_name]['widget'])
        self.refresh()

    def disable_icon(self, icon_name):
        if icon_name not in self.icons or not self.icons[icon_name]['enabled']:
            pass

        self.icons[icon_name]['enabled'] = False
        self.remove_widget(self.icons[icon_name]['widget'])
        self.refresh()

    def refresh(self):
        count = 0
        size = self.height/2
        for icon in (i for i in self.icons if self.icons[i]['enabled']):
            x = self.width - size*5/4 - count*size*1/2 - count*size
            y = self.y + self.height/2 - size/2
            self.icons[icon]['widget'].size = size, size
            self.icons[icon]['widget'].pos = x, y
            count += 1


class MainWidget(Widget):
    base_w = NumericProperty(640)
    base_h = NumericProperty(480)
    header = ObjectProperty(None)


class RecentUsedAppsList(Widget):
    recently_used_apps = ListProperty()

    def on_recently_used_apps(self):
        self.build()


class MainApp(App):
    def build(self):
        Window.size = (320, 240)
        return MainWidget()


if __name__ == '__main__':
    MainApp().run()
