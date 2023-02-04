from kivymd.app import MDApp, Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty
from api import gen_5_images

# --- this changes the app's default background --- #
Window.clearcolor = (.9, .9, .9, 1)
Window.size = (400, 500)

class HomeScreen(Screen):
    source = StringProperty()
    def __init__(self, **kwargs): 
        super(HomeScreen, self).__init__(**kwargs)
        self.text = 'dog'

    def get_text(self):
        self.text = self.ids.input.text

class ResultsScreen(HomeScreen):
    source = StringProperty()
    def on_enter(self, *args):
        # gets run when manager property is changed
        self.urls = gen_5_images(self.manager.get_screen('home').text)
        self.source = self.urls[0]
        
class Main(MDApp):
    def build(self):
        Builder.load_file("layout.kv")
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ResultsScreen(name='results'))
        return sm

Main().run()

