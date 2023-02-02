from kivymd.app import MDApp, Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty
from api import gen_5_images

# --- this changes the app's default background --- #
Window.clearcolor = (.9, .9, .9, 1)
Window.size = (400, 500)

urls = 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-2P7RBkMj286pwFp2tBL0Pdbe/user-U0RAcpr0hRCA6ZDNuci8CxE7/img-3KLEz8jb1UQnTchhtFueUD8L.png?st=2023-02-02T00%3A55%3A16Z&se=2023-02-02T02%3A55%3A16Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-02-01T21%3A21%3A37Z&ske=2023-02-02T21%3A21%3A37Z&sks=b&skv=2021-08-06&sig=L1a8Vxt0CkGqHIGajVyAXZa31i%2BH/xTcXxsnlACQx2U%3D'

class HomeScreen(Screen):
    def gen_images(self):
        text = self.ids.input.text
        self.urls = gen_5_images(text)

class ResultsScreen(Screen):
    source = StringProperty()
    def on_pre_enter(self, *args):
        self.source = urls

class Main(MDApp):
    def build(self):
        Builder.load_file("layout.kv")
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ResultsScreen(name='results'))
        return sm

Main().run()