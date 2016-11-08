from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window

from gui.Header import Header


class State:
    pass


class MainWidget(Widget):
    base_w = 640
    base_h = 480
    state = StringProperty("Home")
    header = Header()

    def load_page(self, page):
        print(page)

class MainApp(App):

    def build(self):
        Window.size = (320, 240)
        return MainWidget()


if __name__ == '__main__':
    MainApp().run()
