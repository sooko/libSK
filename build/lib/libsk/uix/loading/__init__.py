from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty, DictProperty,ListProperty
Builder.load_string("""
<LoadingCircle>:
    Widget:
        pos_hint: {'center_x': 0.5,'center_y': 0.5}
        size_hint: 1*root.scale/100 , 1*root.scale/100
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

""")
class LoadingCircle(FloatLayout):
    color=ListProperty([1,1,1,1])
    background_color=ListProperty([1,1,1,.2])
    transition="in_sine"
    angle=ListProperty([0,0])
    anim_speed=NumericProperty(.8)
    scale=NumericProperty(30)
    line_width=NumericProperty(dp(3))
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

# from kivy.app import App
# class LoadingApp(App):
#     def build(self):
#         return LoadingCircle()


# if __name__=="__main__":
#     LoadingApp().run()

    