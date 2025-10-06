from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from datetime import datetime
import random

class StrongLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.label = Label(text="🕓 Az idő: betöltés alatt...", font_size=28)
        self.button = Button(text="Frissíts színt 🎨", font_size=24)
        self.button.bind(on_press=self.change_color)
        self.add_widget(self.label)
        self.add_widget(self.button)
        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, *args):
        self.label.text = f"🕓 Az idő: {datetime.now().strftime('%H:%M:%S')}"

    def change_color(self, instance):
        self.button.background_color = [random.random(), random.random(), random.random(), 1]

class StrongApp(App):
    def build(self):
        return StrongLayout()

if __name__ == "__main__":
    StrongApp().run()

