from kivy.app import App
from kivy.uix.label import Label

class ZiniaApp(App):
    def build(self):
        return Label(text='Hello from Zinia Voice Assistant!')

if __name__ == '__main__':
    ZiniaApp().run()
