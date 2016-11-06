from kivy.app import App
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window


class BaseWidget(Widget):
    base_x = NumericProperty(640)
    base_y = NumericProperty(480)

    def __init__(self):
        super(Widget, self).__init__()


class Header(BaseWidget):
    def __init__(self, **kwargs):
        super(BaseWidget, self).__init__(**kwargs)
        print(self)


class MainWidget(BaseWidget):
    header = ObjectProperty(None)

    def __init__(self, **kwargs):
        self.state = "Menu"
        super(BaseWidget, self).__init__(**kwargs)


class RecentUsedAppsList(BaseWidget):
    def __init__(self, **kwargs):
        pass


class MainApp(App):
    def build(self):
        # Window.size = (640, 480)
        Window.size = (320, 240)
        return MainWidget()


if __name__ == '__main__':
    MainApp().run()
