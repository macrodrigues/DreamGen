from kivymd.app import MDApp, Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from api import gen_5_images

# --- this changes the app's default background --- #
Window.clearcolor = (.9, .9, .9, 1)
Window.size = (400, 500)

class HomeScreen(Screen):
    def gen_images(self):
        text = self.ids.input.text
        res = gen_5_images(text)
        print(res)


class ResultsScreen(Screen):
    pass


class Main(MDApp):
    def build(self):
        Builder.load_file("layout.kv")
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ResultsScreen(name='results'))
        return sm

Main().run()