from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from kivy.properties import ListProperty,StringProperty,NumericProperty,ColorProperty
from kivy.metrics import dp
Builder.load_string("""
<Cart>:
    canvas:
        Color:
            rgba: root.shadow_color
        BoxShadow:
            pos: self.pos
            size: self.size
            offset:root.offset
            spread_radius: root.spread_radius#-20, -20
            border_radius: root.border_radius#10, 10, 10, 10
            blur_radius: root.blur_radius#80 
        Color:
            rgba: root.background_color
        RoundedRectangle:
            size: self.size[0], self.size[1]
            pos: self.pos
            radius:root.radius
                    

""")
class Cart(FloatLayout):
    radius=ListProperty([dp(5),dp(5),dp(5),dp(5)])
    offset=ListProperty([0, -10])
    spread_radius= ListProperty([-10, -10])
    border_radius= ListProperty([10, 10, 10, 10])
    blur_radius= NumericProperty(30)
    background_color=ColorProperty([.2,.2,.2,1])
    shadow_color=ColorProperty([1,1,1,1])
    
    def __init__(self, **kwargs):
        super(Cart,self).__init__(**kwargs)
