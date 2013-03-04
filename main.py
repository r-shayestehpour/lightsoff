from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from math import sqrt

buttons = []

class LightsOff_Button:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radious = 50
        self.state = False
    
    def IsInButton(touch, self):
        if sqrt((touch.x - self.x)**2 + (touch.y - self.y)**2) < self.size:
            return True
        return False
'''
class LightsOff_InitScreen(Widget):
    def draw_background():
        print 'inastance made'        
        Color(1, 1, 1)
        for i in buttons:
            print 'drawn', i.x, i.y, i.radious
            Ellipse(pos = (i.x, i.y), size = (i.radious, i.radious)) '''

class LightsOff_GameWidget(Widget):
    def init(self):
        canvas_1 = self.canvas
        with canvas_1:
            Color(1, 1, 1)
            for i in buttons:
                print 'drawn', i.x, i.y, i.radious
                Ellipse(pos = (i.x, i.y), size = (i.radious, i.radious))
        return self

    def on_touch_down(self, touch):
#        self.init()
        canvas_2 = self.canvas
        with canvas_2:
            Color(1, 1, 0)
            Ellipse(pos = (100, 100), size = (30, 30))
            print touch

class LightsOff_GameApp(App):
    def build(self):
        for i in range(1, 6):
            for j in range(1, 6):
                tmp = LightsOff_Button()
                tmp.x = i * 50
                tmp.y = j * 50
                buttons.append(tmp)
        #init = LightsOff_InitScreen()
        #init.draw_background()

        return LightsOff_GameWidget().init()        

if (__name__ == '__main__'):
    LightsOff_GameApp().run() 
