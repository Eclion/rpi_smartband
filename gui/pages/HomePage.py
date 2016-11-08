from kivy.properties import ListProperty
from kivy.uix.widget import Widget


class HomePage(Widget):
    # composed of one Label "Apps" and 4 sub labels which are the latest apps used
    # could have at least 4 recent apps

    def on_pos(self, instance, value):
        self.icon.pos = value
        # reposition each sub components

    def on_size(self, instance, value):
        self.icon.size = value
        # resize each sub components


class RecentUsedAppsList(Widget):
    recently_used_apps = ListProperty()

    def on_recently_used_apps(self):
        self.build()