from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty, DictProperty,ListProperty
Builder.load_string("""
<LoadingCircle>:
    BoxLayout:
        orientation: 'vertical'
        size_hint:1,None
        height:self.minimum_height
        pos_hint: {'center_x': 0.5,'center_y': 0.7}
        Widget:
            size_hint:None,None
            pos_hint: {'center_x': 0.5,'center_y': 0.5}
            size:min(root.size)*root.scale/100 , min(root.size)*root.scale/100
            
            canvas:
                Color:
                    rgba: root.background_color
                Line:
                    width: root.line_width*1.8
                    circle:
                        (self.center_x, self.center_y, min(self.width, self.height)
                        /2)
                    cap:"none"
                Color:
                    rgba: root.color
                Line:
                    width: root.line_width
                    circle:
                        (self.center_x, self.center_y, min(self.width, self.height)
                        /2,root.angle[0],root.angle[1])
                    cap:"none"
        Label:
            size_hint:1,None
            height:dp(100)
            text: root.loading_text
            font_size: dp(18)
        
    

""")
class LoadingCircle(FloatLayout):
    color=ListProperty([1,1,1,1])
    background_color=ListProperty([1,1,1,.2])
    transition="in_sine"
    angle=ListProperty([0,0])
    anim_speed=NumericProperty(.8)
    scale=NumericProperty(20)
    line_width=NumericProperty(dp(3))
    loading_text=StringProperty("")

    anim=None
    def __init__(self, **kwargs):
        super(LoadingCircle,self).__init__(**kwargs)
        self.anim=Animation(angle=[0,360],duration=self.anim_speed,t=self.transition)
        self.anim+=Animation(angle=[0,360],duration=.1,t=self.transition)
        self.anim+=Animation(angle=[360,360],duration=self.anim_speed,t=self.transition)
        self.anim+=Animation(angle=[360,360],duration=self.anim_speed,t=self.transition)
        self.anim+=Animation(angle=[0,0],duration=0,t=self.transition)
        self.anim.repeat=True
        self.anim.start(self)
    def on_parent(self,a,b):
        if self.anim:
            if not b:
                print("close_anim")
                self.anim.cancel_all(self)