from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty,ListProperty,ColorProperty,NumericProperty
from kivy.animation import Animation
from kivy.lang.builder import Builder
from kivy.clock import  Clock
import os.path
from kivy.resources import resource_add_path
from kivy.metrics import dp
resource_add_path(os.path.dirname(__file__))
Builder.unload_file("toast.kv")
Builder.load_file("toast.kv")
                    

class Toast(FloatLayout):
    toast_icon="/home/sooko/prj/prj_cursor/libsk/libsk/assets/images/s_small.png"
    toast_y=NumericProperty(.1)
    background_color=ColorProperty([.1,.1,.1,1])
    toast_text =StringProperty("download failed")
    anim_value=NumericProperty(0)

    def __init__(self, **kwargs):
        super(Toast,self).__init__(**kwargs)
        
        # self.do_toast("loading...",2)
    def do_toast(self,toast_text,duration):
        self.toast_text=toast_text
        anim=Animation(anim_value=100,duration=.3)
        anim.start(self)
        Clock.schedule_once(self.end_toast,1+duration)
    def end_toast(self,dt):
        self.anim_value=0
    
        
