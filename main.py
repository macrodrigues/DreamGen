from kivymd.app import MDApp, Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window

# --- this changes the app's default background --- #
Window.clearcolor = (.9, .9, .9, 1)
Window.size = (400, 500)

class Intro(MDBoxLayout):
    pass

class MyHome(MDBoxLayout):
    pass

class MyApp(MDApp):
    pass

MyApp().run()