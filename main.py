from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse

class Button:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radious = 50
        self.state = False

    def IsInButton(touch, self):
        if abs(touch.x - self.x) < self.size and abs(touch);

class LightsOffWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 1, 0)
            Ellipse(pos = (100, 100), size = (30, 30))
            print touch

class LightsOffGame(App):
    def build(self):
        return LightsOffWidget()        

if (__name__ == '__main__'):
    LightsOffGame().run()
   
