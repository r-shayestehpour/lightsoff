from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from math import sqrt

buttons = []

class Button:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radious = 50
        self.state = False
    
    def IsInButton(touch, self):
        if sqrt((touch.x - self.x)**2 + (touch.y - self.y)**2) < self.size:
            return True
        return False

class LightsOffWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 1, 0)
            Ellipse(pos = (100, 100), size = (30, 30))
            print touch

class LightsOffGame(App):
    def build(self):
        for i in range(1, 6):
            for j in ragne(1, 6):
                tmp = Button()
                tmp.x = i * 100
                tmp.y = j * 100
                buttons.append(tmp)
        
        for i in buttons:
        

        return LightsOffWidget()        

if (__name__ == '__main__'):
    LightsOffGame().run()
   
