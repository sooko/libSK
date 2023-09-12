from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty,ListProperty,ColorProperty,NumericProperty
from kivy.animation import Animation
from kivy.lang.builder import Builder
from kivy.clock import  Clock
Builder.load_string("""
<Toast>:
    
    pos_hint: {'center_x': 0.5,'center_y': 0.5}
    Button:
        id:btn
        size_hint:.7,.05
        pos_hint: {'center_x': 0.5,'center_y': 0.1}
        background_color:0,0,0,0
    StencilView:
        size_hint:None,None
        size:btn.size[0]*root.anim_value/100,btn.size[1]
        x:btn.x
        y:btn.y
        FloatLayout:
            pos:btn.pos
            size:btn.size
            BoxLayout:
                canvas:
                    Color:
                        rgba: [1, 1,1, .1]
                    RoundedRectangle:
                        size: self.size[0]+dp(30), self.size[1]+dp(30)
                        pos: self.pos[0]-dp(10),self.pos[1]-dp(10)
                        radius:dp(5),dp(5),dp(5),dp(5)
                    
                pos_hint:{"center_x":.5,"center_y":.5}
                size_hint:None,1
                width:self.minimum_width
                FloatLayout:
                    size_hint:None,1
                    width:dp(20)
                    Widget:
                        pos_hint:{"center_x":.5,"center_y":.5}
                        size_hint:None,None
                        size:min(self.parent.size),min(self.parent.size)
                        canvas:
                            Color:
                            Rectangle:
                                size: self.size[0], self.size[1]
                                pos: self.pos
                                source:root.toast_icon
                Widget:
                    size_hint:None,1
                    width:dp(5)
                Label:     
                    size_hint:None,1
                    width:self.texture_size[0]
                    background_color:0,0,0,0
                    text:root.toast_text

    
    

""")
                    

class Toast(FloatLayout):
    toast_icon="libsk/assets/images/s.png"
    toast_y=NumericProperty(.1)
    background_color=ColorProperty([.1,.1,.1,1])
    toast_text =StringProperty("download failed")
    anim_value=NumericProperty(0)

    def __init__(self, **kwargs):
        super(Toast,self).__init__(**kwargs)
        
        # self.do_toast("loading...",2)
    def do_toast(self,toast_text,duration):
        self.toast_text=toast_text
        anim=Animation(anim_value=100,duration=1)
        anim.start(self)
        Clock.schedule_once(self.end_toast,1+duration)
    def end_toast(self,dt):
        self.anim_value=0
    
        
