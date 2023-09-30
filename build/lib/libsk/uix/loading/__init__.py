from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty, DictProperty,ListProperty
import os.path
from kivy.resources import resource_add_path
resource_add_path(os.path.dirname(__file__))
Builder.unload_file("loading.kv")
Builder.load_file("loading.kv")

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